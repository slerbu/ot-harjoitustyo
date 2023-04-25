import sys
from game_code.board import Board
import pygame

from pygame.locals import QUIT

pygame.init()
width = 720
height = 720
size = (width, height)
display = pygame.display.set_mode(size)
pygame.display.set_caption("Chess game")
gameboard = Board(width, height)
gameboard.setup_pieces()

def draw(screen):
    gameboard.draw_board(screen)
    pygame.display.update()

draw(display)
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gameboard.mouse_click(mouse_x, mouse_y)
                draw(display)
        