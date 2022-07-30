from turtle import width
import pygame
import time
from sys import exit


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
redghost = pygame.image.load("redghost.png")
redghost.set_colorkey((255,255,255))
redghost = pygame.transform.scale(redghost,(30,30))
redghost_Rect = redghost.get_rect()

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
    







board1 = board(width,height,screen)
pacman1 = pacman(screen, board1)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
    screen.fill((0,0,0))
    board1.draw()
    screen.blit(redghost, redghost_Rect)
    pacman1.move()
    pacman1.draw()
    pygame.display.update()
    
    clock.tick(60)


