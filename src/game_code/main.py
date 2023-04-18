import sys
from board import Board
import pygame

from pygame.locals import QUIT

pygame.init()
width = 640
height = 640
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess game")
gameboard = Board(width, height)




def draw(screen):
	

	gameboard.draw_board(screen)

	pygame.display.update()
    

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gameboard.mouse_click(mouse_x, mouse_y)
                
                
            
        gameboard.draw_board(screen)
        pygame.display.update()
        draw(screen)

    
main()
