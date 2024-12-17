import pygame

screen = pygame.display.set_mode((1000, 1000))

def pozycja_pola_wg_Franka(x, y, offset, a):
    xPos = ((x-1)*a + x*offset*2 - offset)
    yPos = ((y-1)*a + y*offset*2 - offset)
    return (xPos, yPos)

running = True
black = (0,0,0)
white = (255, 255, 255)
a = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 1025:
            white = (0,255,0)
            
    screen.fill(black)

    for i in range(1, 10):
        for j in range(1,10):
            myPosition = pozycja_pola_wg_Franka(i,j,10,a)
            pygame.draw.rect(screen, white, (myPosition[0],myPosition[1],a,a))
    
    pygame.display.flip()

pygame.quit()
