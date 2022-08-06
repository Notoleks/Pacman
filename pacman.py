from turtle import width
import pygame
import time
from sys import exit
import random

pygame.init()
width,height = 600,600

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
# board = pygame.image.load("pacman grid.png")
# board.set_colorkey((0,0,0))
# board = pygame.transform.scale(board,(width,height))


# print(board.get_alpha(),board.get_colorkey())
# board_Rect = board.get_rect()
# board_mask = pygame.mask.from_threshold(board, (0,255,0))
# # pacman = pygame.image.load("pacman.jpg")
# #pacman = pygame.transform.scale(pacman,(30,30))
# pacman.set_colorkey((255,255,255))

# pacman_Rect = pacman.get_rect()

class redghost(pygame.sprite.Sprite):
    def __init__(self, board, image, *groups):
        super().__init__(groups)
        self.image = pygame.image.load(image)
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect(center=(300,330))
        self.direction = 0
        self.board = board
    def update(self):
        if self.direction == 0:
            self.rect.x += 2
        elif self.direction == 90:
            self.rect.y -= 2
        elif self.direction == 180:
            self.rect.x -= 2
        elif self.direction == 270:
            self.rect.y += 2

        if pygame.sprite.collide_mask(self, self.board):

            if self.direction == 0:
                self.rect.x -= 2
            elif self.direction == 90:
                self.rect.y += 2
            elif self.direction == 180:
                self.rect.x += 2
            elif self.direction == 270:
                self.rect.y -= 2
            choice = random.randint(0,3)
            if choice == 0:
                self.direction = 0
            elif choice == 1:
                self.direction = 90
            elif choice == 2:
                self.direction = 180
            elif choice == 3:
                self.direction = 270


class board(pygame.sprite.Sprite):
    def __init__(self, width, height, screen) -> None:

        super().__init__()
        self.board = pygame.image.load("pacman grid.png")
        self.board.set_colorkey((0,0,0))
        self.board = pygame.transform.scale(self.board,(width,height))
        self.rect = self.board.get_rect()
        self.mask = pygame.mask.from_surface(self.board)
        self.screen = screen


    def draw(self):
        self.screen.blit(self.board, self.rect)


        

class pacman(pygame.sprite.Sprite):
    def __init__(self, screen, board) -> None:

        super().__init__()
        self.pacman = pygame.image.load("pacman.png").convert()
        self.pacman.set_colorkey((255,255,0))
        pygame.Surface.set_colorkey(self.pacman,(255,255,255))
        self.pacman = pygame.transform.scale(self.pacman, (50 , 28))
        self.rect = self.pacman.get_rect()
        self.rect.center = (340,330)
        self.mask = pygame.mask.from_surface(self.pacman)
        self.direction = 0
        self.screen = screen
        self.board = board

        
    


    def draw(self):
        self.screen.blit(self.pacman, self.rect)



    def move(self):
        # offset_x = self.pacman_Rect[0] - self.board_Rect[0]
        # offset_y = self.pacman_Rect[1] - self.board_Rect[1]
        # overlap = self.mask.overlap(self.board_mask,(offset_x, offset_y))
        
        # if overlap:
        #     print(self.pacman_Rect[0])
        if self.direction == 0:
            self.rect.x += 2
        elif self.direction == 90:
            self.rect.y -= 2
        elif self.direction == 180:
            self.rect.x -= 2
        elif self.direction == 270:
            self.rect.y += 2

        if pygame.sprite.collide_mask(self, self.board):
            if self.direction == 0:
                self.rect.x -= 2
            elif self.direction == 90:
                self.rect.y += 2
            elif self.direction == 180:
                self.rect.x += 2
            elif self.direction == 270:
                self.rect.y -= 2
        


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.direction = 90
        elif pressed[pygame.K_a]:
            self.direction = 180
        elif pressed[pygame.K_s]:
            self.direction = 270
        elif pressed[pygame.K_d]:
            self.direction = 0
    






characters = pygame.sprite.Group()
board1 = board(width,height,screen)
pacman1 = pacman(screen, board1)
redghost1 = redghost(board1, "orangeghost.png", characters)
redghost2 = redghost(board1, "redghost.png", characters)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
    screen.fill((0,0,0))
    board1.draw()
    
    pacman1.move()
    pacman1.draw()
    characters.draw(screen)
    characters.update()
    pygame.display.update()
    
    clock.tick(60)


