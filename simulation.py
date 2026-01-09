import pygame
import math
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 1000))

running = True
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)

x_r = 100
y_r = 200
x_a = 500
y_a = 500
F_x = 0
F_y = 0

v_x = 0
v_y = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)
    
    m_r = 200
    m_a = 50
    r = math.sqrt((x_r-x_a)**2 + (y_r-y_a)**2)
    G = 500
    F = G * m_r * m_a / r**2
    alpha = math.atan((y_a - y_r)/(x_a - x_r))
    F_x = math.cos(alpha) * F
    F_y = math.sin(alpha) * F
    
    screen.fill(black)

    pygame.draw.circle(screen, white, (x_r, y_r), 20)
    pygame.draw.circle(screen, green, (x_a, y_a), 100)
    pygame.draw.line(screen, white, (x_r, y_r), (x_r + F_x, y_r + F_y))
    
    pygame.display.flip()
    print(F_y, alpha)
    a_x = F_x/m_r
    a_y = F_y/m_r
    
    v_x += a_x
    v_y += a_y
    
    x_r += v_x
    y_r += v_y
    
pygame.quit()
