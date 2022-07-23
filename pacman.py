import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
board = pygame.image.load("pacman grid.png")
board.set_colorkey((0,0,0))
board = pygame.transform.scale(board,(1100,1100))


print(board.get_alpha(),board.get_colorkey())
board_Rect = board.get_rect()
board_mask = pygame.mask.from_threshold(board, (0,255,0))
pacman = pygame.image.load("pacman.jpg")
#pacman = pygame.transform.scale(pacman,(30,30))
pacman.set_colorkey((255,255,255))

pacman_Rect = pacman.get_rect()
redghost = pygame.image.load("redghost.png")
redghost.set_colorkey((255,255,255))
redghost = pygame.transform.scale(redghost,(30,30))
redghost_Rect = redghost.get_rect()


class pacman:
    def __init__(self, screen, board, board_Rect, board_mask) -> None:
        self.pacman = pygame.image.load("pacman.jpg").convert()
        pygame.Surface.set_colorkey(self.pacman,(255,255,0))
        self.pacman = pygame.transform.scale(self.pacman, (20 , 20))
        self.pacman_Rect = self.pacman.get_rect()
        self.pacman_Rect.center = (200,220)
        self.mask = pygame.mask.from_surface(self.pacman)
        self.direction = 0
        self.screen = screen
        self.board, self.board_Rect, self.board_mask = board, board_Rect, board_mask

        
    


    def draw(self):
        self.screen.blit(self.pacman, self.pacman_Rect)



    def move(self):
        offset_x = self.pacman_Rect[0] - self.board_Rect[0]
        offset_y = self.pacman_Rect[1] - self.board_Rect[1]
        overlap = self.mask.overlap(self.board_mask,(offset_x, offset_y))
        
        if overlap:
            print(self.pacman_Rect[0])
        if self.direction == 0:
            self.pacman_Rect.x += 2
        elif self.direction == 90:
            self.pacman_Rect.y -= 2
        elif self.direction == 180:
            self.pacman_Rect.x -= 2
        elif self.direction == 270:
            self.pacman_Rect.y += 2
        if pacman_Rect.colliderect(board_Rect):
            print("collision")

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.direction = 90
        elif pressed[pygame.K_a]:
            self.direction = 180
        elif pressed[pygame.K_s]:
            self.direction = 270
        elif pressed[pygame.K_d]:
            self.direction = 0
    








pacman1 = pacman(screen, board, board_Rect, board_mask)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
    screen.fill((0,0,0))
    screen.blit(board, board_Rect)
    screen.blit(redghost, redghost_Rect)
    pacman1.move()
    pacman1.draw()
    pygame.display.update()
    
    clock.tick(60)


