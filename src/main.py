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
    print(gameboard.create_squares()[0].x)

    

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    
main()
