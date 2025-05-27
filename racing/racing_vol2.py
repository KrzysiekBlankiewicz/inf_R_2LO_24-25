import pygame
import math

forward = 0
backward = 1
left = 2
right = 3
black = (0, 0, 0)
white = (255, 255, 255)
line_len = 50

def deg_to_rad(deg):
    return deg/360 * (2*math.pi)

class Car:
    def __init__(s, position, color):
        s.x, s.y = position
        s.color = color
        s.r = 30
        s.v = 10
        s.rotation = 0
        s.vel_angl = deg_to_rad(10)

    def turn(s, direction):
        if direction == left:
            s.rotation += s.vel_angl
        if direction == right:
            s.rotation -= s.vel_angl
        
    def move(s, direction):
        if direction == forward:
            s.x += s.v * math.cos(s.rotation)
            s.y += s.v * math.sin(s.rotation)
        if direction == backward:
            s.x -= s.v * math.cos(s.rotation)
            s.y -= s.v * math.sin(s.rotation)
            
    def motion(s, direction):
        if direction == forward or direction == backward:
            s.move(direction)
        elif direction == left or direction == right:
            s.turn(direction)
        else:
            pass
        
    def draw(s, window):
        pygame.draw.circle(window, s.color, (s.x, s.y), s.r)
        pygame.draw.line(window, s.color, (s.x, s.y),(s.x + line_len*math.cos(s.rotation), s.y + line_len*math.sin(s.rotation)))
        
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

size = 500
running = True

pygame.init()
window = pygame.display.set_mode((size, size))
car = Car((100, 100), white)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            car.motion(key_to_direct(e.key))

    window.fill(black)
    car.draw(window)
    pygame.display.flip()
    
pygame.quit()
