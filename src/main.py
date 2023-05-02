import sys
import pygame
from game_code.board import Board


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
    pygame.display.flip()


draw(display)
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gameboard.mouse_click(mouse_x, mouse_y, gameboard)

                draw(display)
