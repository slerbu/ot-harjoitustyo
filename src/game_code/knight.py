import pygame
from game_code.piece import Piece


class Knight(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)
        self.type = "Knight"
        self.image = pygame.image.load(
            f"src/game_code/imgs/{self.color}_{self.type.lower()}.png")
        self.image = pygame.transform.scale(
            self.image, (int(board.tile_width), int(board.tile_height)))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] * board.tile_width
        self.rect.y = self.pos[1] * board.tile_height

    def get_legal_moves(self, board):
        legal_moves = []
        if self.pos[0] - 2 >= 0 and self.pos[1] - 1 >= 0:
            legal_moves.append((self.pos[0]-2, self.pos[1]-1))
        if self.pos[0] - 2 >= 0 and self.pos[1] + 1 <= 7:
            legal_moves.append((self.pos[0]-2, self.pos[1]+1))

        if self.pos[0] + 2 >= 0 and self.pos[1] + 1 >= 0:
            legal_moves.append((self.pos[0]+2, self.pos[1]+1))

        if self.pos[0] + 2 >= 0 and self.pos[1] - 1 >= 0:
            legal_moves.append((self.pos[0]+2, self.pos[1]-1))

        if self.pos[0] - 1 >= 0 and self.pos[1] - 2 >= 0:
            legal_moves.append((self.pos[0]-1, self.pos[1]-2))
        if self.pos[0] - 1 >= 0 and self.pos[1] + 2 <= 7:
            legal_moves.append((self.pos[0]-1, self.pos[1]+2))

        if self.pos[0] + 1 >= 0 and self.pos[1] + 2 >= 0:
            legal_moves.append((self.pos[0]+1, self.pos[1]+2))

        if self.pos[0] + 1 >= 0 and self.pos[1] - 2 >= 0:
            legal_moves.append((self.pos[0]+1, self.pos[1]-2))

        return legal_moves
