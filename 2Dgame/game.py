import pygame
import random


def directions(x, size):
    if x == 1:
        return (0, size)
    elif x == 2:
        return (size, 0)
    elif x == 3:
        return (0, -size)
    elif x == 4:
        return (-size, 0)


def isMovePossible(pos_x, pos_y, obstacles, size):
    temporary = pygame.Rect(pos_x - size, pos_y - size, size*2, size*2)
    for obstacle in obstacles:
        temp_obstacle = pygame.Rect(obstacle.x, obstacle.y, obstacle.w, obstacle.h)
        if temporary.colliderect(temp_obstacle):
            return False
    return True
            

class Player:
    def __init__(self, startX, startY, color):
        self.x = startX
        self.y = startY
        self.color = color

    def move(self, dir_x, dir_y, obstacles, player_size):
        temp_x = self.x + dir_x
        temp_y = self.y + dir_y
        if isMovePossible(temp_x, temp_y, obstacles, player_size) == True:
            self.x += dir_x
            self.y += dir_y

    
    def draw(self, window, player_size):
        pygame.draw.circle(window, self.color, (self.x, self.y), player_size)

class Obstacle:
    def __init__(self, startX, startY, width, height, color):
        self.x = startX
        self.y = startY
        self.w = width
        self.h = height
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
        
class Enemy:
    def __init__(self, startX, startY, color):
        self.x = startX
        self.y = startY
        self.color = color
        self.move_delay = 20
        self.move_counter = 0

    def move(self, obstacles, enemy_size):
        self.move_counter += 1
        if self.move_counter < self.move_delay:
            return
        self.move_counter = 0
        
        direction = random.randint(1,4)
        dir_x, dir_y = directions(direction, enemy_size)
        temp_x = self.x + dir_x
        temp_y = self.y + dir_y
        if isMovePossible(temp_x, temp_y, obstacles, enemy_size) == True:
            self.x += dir_x
            self.y += dir_y
    
    def draw(self, window, enemy_size):
        pygame.draw.circle(window, self.color, (self.x, self.y), enemy_size)

class Bullet:
    def __init__(self, pos_x, pos_y, speed=3):
        self.x = pos_x
        self.y = pos_y
        self.size = 5
        self.speed = speed
        self.color = (0, 0, 0)

    def move(self):
        self.y -= self.speed

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

    def get_rect(self):
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size*2, self.size*2)


size = 800
clock = pygame.time.Clock()
running = True

pygame.init()
screen = pygame.display.set_mode((size, size))

player_size = 25
player_color = (0, 0, 255)
myPlayer = Player(400, 400, player_color)

enemy_size = 25
enemy_color = (255, 0, 255)
enemies = [
    Enemy(300, 300, enemy_color),
    Enemy(500, 200, enemy_color)
]

obstacle_width = 100
obstacle_height = 200
obstacle_color = (255, 0, 0)
obstacles = [
    Obstacle(100, 100, obstacle_width, obstacle_height, obstacle_color),
    Obstacle(600, 600, obstacle_width, obstacle_height, obstacle_color)
]

bullets = []


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                myPlayer.move(0, -player_size, obstacles, player_size)
            if event.key == pygame.K_a:
                myPlayer.move(-player_size, 0, obstacles, player_size)
            if event.key == pygame.K_s:
                myPlayer.move(0, player_size, obstacles, player_size)
            if event.key == pygame.K_d:
                myPlayer.move(player_size, 0, obstacles, player_size)
            if event.key == pygame.K_SPACE:
                bullet = Bullet(myPlayer.x, myPlayer.y)
                bullets.append(bullet)
                
    for enemy in enemies:
        enemy.move(obstacles, enemy_size)

    for bullet in bullets:
        bullet.move()

    for bullet in bullets[:]:
        bullet_rect = bullet.get_rect()
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy.x - enemy_size, enemy.y - enemy_size, enemy_size*2, enemy_size*2)
            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    player_rect = pygame.Rect(myPlayer.x - player_size, myPlayer.y - player_size, player_size*2, player_size*2)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy.x - enemy_size, enemy.y - enemy_size, enemy_size * 2, enemy_size * 2)
        if player_rect.colliderect(enemy_rect):
            running = False
    
    screen.fill((255,255,255))
    
    myPlayer.draw(screen, player_size)
    for enemy in enemies:
        enemy.draw(screen, enemy_size)
    for obs in obstacles:
        obs.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
        
    pygame.display.flip()
    clock.tick(35)
    
pygame.quit()



            
