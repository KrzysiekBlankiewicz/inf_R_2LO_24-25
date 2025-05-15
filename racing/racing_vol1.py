import pygame
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
        s.r = 20
        s.v = 10
        
    def move(s, direction):
        if direction == up:
            s.y -= s.v
        if direction == down:
            s.y += s.v
        if direction == left:
            s.x -= s.v
        if direction == right:
            s.x += s.v
            
    def draw(s, window):
        pygame.draw.circle(window, s.color, (s.x, s.y), s.r)

def key_to_direct(key):
    if key == pygame.K_w:
        return up
    if key == pygame.K_s:
        return down
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
            car.move(key_to_direct(e.key))

    window.fill(black)
    car.draw(window)
    pygame.display.flip()
    
pygame.quit()
