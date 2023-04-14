import pygame, sys
from pygame.locals import *
from board import Board
def main():
    pygame.init()
    width = 640
    height = 640
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chess game")
    gameboard = Board(width, height)
    gameboard.create_squares()
    gameboard.draw_board(screen)
    pawn = pygame.image.load("src/code/data/light_pawn.png")
    bishop = pygame.image.load("src/code/data/light_bishop.png")
    rook = pygame.image.load("src/code/data/light_rook.png")
    for i in range(8):
        screen.blit(pawn, (i*80, 75))
    screen.blit(bishop, (160, 0))
    screen.blit(bishop, (400, 0))
    screen.blit(rook, (0, 0))
    screen.blit(rook, (560, 0))
    
    

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    
main()
