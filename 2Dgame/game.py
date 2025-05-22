import pygame

# let's assume that all objects are represented by circles

def isMovePossible(movingAgent, obstacles):
    # for each obstacle:
    #       if distance between obstacle and movingAgent is less than ...
    #               return False (position is illegal)
    # return True (position is ok)
    pass

class Player:
    def __init__(self, startX, startY, color):
        pass

    def move(self, direction):
        pass
        # before changing position call isMovePossible() to check if move is allowed
    
    def draw(self, window):
        pass

class Obstacle:
    def __init__(self, startX, startY, color):
        pass

    def draw(self, window):
        pass

class Enemy:
    def __init__(self, startX, startY, color):
        pass

    def move(self):
        # move in random direction
        # before changing position call isMovePossible() to check if move is allowed
        pass
    
    def draw(self, window):
        pass


size = 800
running = True

pygame.init()
screen = pygame.display.set_mode((size, size))

# create variables for Player, Enemy, Obstacle
# ex. myPlayer = Player(100, 100, (0, 0, 0))

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN
            if event.key == pygame.K_w:
                # move player
                pass
            # ...other keys
            
    # move enemy (no mater if any key was pressed or not)
    
    # screen.fill()
    # draw Player, Enemy, Obstacle
    pygame.display.flip()
    
pygame.quit()



            
