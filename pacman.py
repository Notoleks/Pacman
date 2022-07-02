import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
board = pygame.image.load("pacman grid.png")
board = pygame.transform.scale(board,(400,400))
board_Rect = board.get_rect()
pacman = pygame.image.load("pacman.jpg")
pacman = pygame.transform.scale(pacman,(30,30))
pacman_Rect = pacman.get_rect()
redghost = pygame.image.load("redghost.png")
redghost = pygame.transform.scale(redghost,(30,30))
redghost_Rect = redghost.get_rect()

class pacman:
    def __init__(self, screen) -> None:
        self.pacman = pygame.image.load("pacman.jpg").convert()
        pygame.Surface.set_colorkey(self.pacman,(255,255,0))
        self.pacman = pygame.transform.scale(self.pacman, (30 , 25))
        self.pacman_Rect = self.pacman.get_rect()
        self.pacman_Rect.center = (200,220)


        self.screen = screen


    def draw(self):
        self.screen.blit(self.pacman, self.pacman_Rect)


    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.pacman_Rect.y -= 2
        if pressed[pygame.K_a]:
            self.pacman_Rect.x -= 2
        if pressed[pygame.K_s]:
            self.pacman_Rect.y += 2
        if pressed[pygame.K_d]:
            self.pacman_Rect.x += 2








pacman1 = pacman(screen)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code

        screen.blit(board, board_Rect)
        screen.blit(redghost, redghost_Rect)
        pacman1.move()
        pacman1.draw()
        pygame.display.update()
        clock.tick(60)


