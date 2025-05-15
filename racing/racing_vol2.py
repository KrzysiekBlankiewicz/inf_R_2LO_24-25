import pygame
import math

up = 0
down = 1
left = 2
right = 3
black = (0, 0, 0)
white = (255, 255, 255)

class Car:
    def __init__(s, position, color):
        s.x, s.y = position
        s.color = color
        s.r = 10
        s.v = 10
        s.rotation = 0
        s.vel_angl = 10 * (2*math.pi)/360

    def turn(s, direction):
        if direction == left:
            s.rotation += s.vel_angl
        if direction == right:
            s.rotation -= s.vel_angl
        
    def move(s, direction):
        pass
            
    def draw(s, window):
        pygame.draw.circle(window, s.color, (s.x, s.y), s.r)
        pygame.draw.line(window, s.color, (s.x, s.y),(s.x + 50*math.cos(s.rotation), s.y + 50*math.sin(s.rotation)))
        
def key_to_direct(key):
    if key == pygame.K_a:
        return left
    if key == pygame.K_d:
        return right

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
            car.turn(key_to_direct(e.key))

    window.fill(black)
    car.draw(window)
    pygame.display.flip()
    
pygame.quit()
