import pygame
import math
import random
pygame.init()

white = (255, 255, 255)
black = (0,0,0)
size = 1000
screen = pygame.display.set_mode([size, size])
forward = 0
backward = 1
left = 2
right = 3

class Player:
    def __init__(s, start_pos):
        s.x = start_pos[0]
        s.y = start_pos[1]
        s.color = white
        s.r = 5
        s.rotation = 0
        s.vel_angl = 0.1
        s.direction = forward
        s.v = 0
        
    def draw(s, window):
        pygame.draw.circle(window, s.color, (s.x, s.y), s.r)

    def turn(s, direction):
        if direction == left:
            s.rotation += s.vel_angl
        if direction == right:
            s.rotation -= s.vel_angl

    def accelerate(s, direction):
        if direction == s.direction:
            s.v += 0.1
        else:
            s.v -= 0.1
    
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

class Wall:
    def __init__(s, start, end):
        s.color = white
        s.start = start
        s.end = end

    def collision_circle(s, center, radius):
        pass
    
    def draw(s, window):
        pygame.draw.line(window, s.color, s.start, s.end)

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
    
p = Player((100, 100))

file = open("walls.txt")
walls = []
for i in range(0, 10):
    list = file.readline().split()
    if len(list) == 0:
        break
    x1 = int(list[0])
    y1 = int(list[1])
    x2 = int(list[2])
    y2 = int(list[3])
    walls.append(Wall((x1, y1), (x2, y2)))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            p.motion(key_to_direct(event.key))

    screen.fill(black)
    p.move()
    p.draw(screen)
    for w in walls:
        w.draw(screen)
    pygame.display.flip()

pygame.quit()
