import pygame


gray = (100, 100, 100)
purple = (128, 0, 128)
black = (0, 0, 0)


sizeX, sizeY = 500, 800


up = 1
down = 2
left = 3
right = 4


pygame.init()
pygame.display.set_caption('Breaking Kart')
window = pygame.display.set_mode((500, 500))


class Car:
    def __init__(self, position):
        self.position = list(position)
        self.radius = 20
        self.velocity = 5

    def move(self, direction):
        if direction == up:
            self.position[1] -= self.velocity
        elif direction == down:
            self.position[1] += self.velocity
        elif direction == left:
            self.position[0] -= self.velocity
        elif direction == right:
            self.position[0] += self.velocity

    def draw(self, surface):
        pygame.draw.circle(surface, black, self.position, self.radius)


def key_to_direct(key):
    if key == pygame.K_UP:
        return up
    elif key == pygame.K_DOWN:
        return down
    elif key == pygame.K_LEFT:
        return left
    elif key == pygame.K_RIGHT:
        return right
    return None


running = True
car = Car(position=(250, 250))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            direction = key_to_direct(e.key)
            if direction:
                car.move(direction)

    window.fill(purple)
    car.draw(window)
    pygame.display.flip()

pygame.quit()