import pygame
import math
import socket

forward = 0
backward = 1
left = 2
right = 3
black = (0, 0, 0)
white = (255, 255, 255)
line_len = 50

def deg_to_rad(deg):
    return deg/360 * (2*math.pi)

def rad_to_deg(rad):
    return (rad * 360) / (2*math.pi)

class Car:
    def __init__(s, position, color):
        s.img = pygame.image.load("car.png")
        s.img = pygame.transform.rotate(s.img, -90)
        s.x, s.y = position
        s.color = color
        s.r = 30
        s.v = 0
        s.rotation = 0
        s.vel_angl = deg_to_rad(10)
        s.direction = forward

    def turn(s, direction):
        if direction == left:
            #s.img = pygame.transform.rotate(s.img, -10)
            s.rotation += s.vel_angl
        if direction == right:
            #s.img = pygame.transform.rotate(s.img, 10)
            s.rotation -= s.vel_angl

    def accelerate(s, direction):
        if direction == s.direction:
            s.v += 2
        else:
            s.v -= 2
    
    def move(s):
        if s.direction == forward:
            s.x += s.v * math.cos(s.rotation)
            s.y -= s.v * math.sin(s.rotation)
        if s.direction == backward:
            s.x -= s.v * math.cos(s.rotation)
            s.y += s.v * math.sin(s.rotation)
            
    def motion(s, direction):
        if direction == forward or direction == backward:
            s.accelerate(direction)
        elif direction == left or direction == right:
            s.turn(direction)
        else:
            pass
        
    def draw(s, window):
        deg_rotation = rad_to_deg(s.rotation)
        #print(s.rotation, deg_rotation)
        temp_img = pygame.transform.rotate(s.img, deg_rotation)
        x = s.x - temp_img.get_rect().width/2
        y = s.y - temp_img.get_rect().height/2
        window.blit(temp_img, (x, y))
        pygame.draw.line(window, s.color, (s.x, s.y),(s.x + line_len*math.cos(s.rotation), s.y - line_len*math.sin(s.rotation)))
        
def key_to_direct(key):
    if key == pygame.K_a:
        return left
    elif key == pygame.K_d:
        return right
    elif key == pygame.K_w:
        return forward
    elif key == pygame.K_s:
        return backward
    else:
        return None

def data_to_direct(data):
    if data == b"left":
        return left
    elif data == b"right":
        return right
    elif data == b"forward":
        return forward
    elif data == b"backward":
        return backward
    else:
        return None

size = 500
running = True
clock = pygame.time.Clock()
pygame.init()
window = pygame.display.set_mode((size, size))
car = Car((100, 100), black)

while running:
    
    clock.tick(30)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            car.motion(key_to_direct(e.key))

    window.fill(white)
    car.move()
    car.draw(window)
    pygame.display.flip()
    
pygame.quit()
