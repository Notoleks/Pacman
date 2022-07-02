import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
board = pygame.image.load("pacman-path.png")
board = pygame.transform.scale(board,(400,400))
board_Rect = board.get_rect()
pacman = pygame.image.load("pacman sprite.jpg")
pacman = pygame.transform.scale(pacman,(30,30))
pacman_Rect = pacman.get_rect()
redghost = pygame.image.load("red ghost.png")
redghost = pygame.transform.scale(redghost,(30,30))
redghost_Rect = redghost.getrect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code

        screen.blit(board, board_Rect)
        screen.blit(pacman, pacman_Rect)
        pygame.display.update()
        clock.tick(60)


