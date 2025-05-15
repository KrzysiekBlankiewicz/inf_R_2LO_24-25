import pygame

class Car:
    def __init__(s):
        pass
    def move(s, direction):
        pass
    def draw(s, window):
        #pygame.draw.circle(window, color, (center), radius)

def key_to_direct(key):

running = True

pygame.init()
window = pygame.display.set_mode((500, 500))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            pass

    window.fill(black)

    pygame.display.flip()
    
pygame.quit()
