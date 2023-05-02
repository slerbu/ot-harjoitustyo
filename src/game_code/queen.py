import pygame
from game_code.piece import Piece


class Queen(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)
        self.type = "Queen"
        self.image = pygame.image.load(
            f"src/game_code/imgs/{self.color}_{self.type.lower()}.png")
        self.image = pygame.transform.scale(
            self.image, (int(board.tile_width), int(board.tile_height)))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] * board.tile_width
        self.rect.y = self.pos[1] * board.tile_height

    def get_legal_moves(self, board):
        legal_moves = []
        for i in range(1, 7):
            if self.pos[0] - i >= 0:
                position = (self.pos[0]-i, self.pos[1])

                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        for i in range(1, 7):
            if self.pos[0] + i <= 7:
                position = (self.pos[0]+i, self.pos[1])

                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        for i in range(1, 7):
            if self.pos[1] - i >= 0:
                position = (self.pos[0], self.pos[1]-i)
                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        for i in range(1, 7):
            if self.pos[1] + i <= 7:
                position = (self.pos[0], self.pos[1]+i)
                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        for i in range(1, 7):
            position = (self.pos[0]-i, self.pos[1]-i)

            if 0 <= self.pos[0] - i <= 7 and 0 <= self.pos[1] - i <= 7:
                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        for i in range(1, 7):
            if 0 <= self.pos[0] + i <= 7 and 0 <= self.pos[1] - i <= 7:
                position = (self.pos[0]+i, self.pos[1]-i)
                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break
        for i in range(1, 7):
            if 0 <= self.pos[0] - i <= 7 and 0 <= self.pos[1] + i <= 7:
                position = (self.pos[0]-i, self.pos[1]+i)
                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        for i in range(1, 7):
            if 0 <= self.pos[0] + i <= 7 and 0 <= self.pos[1] + i <= 7:
                position = (self.pos[0]+i, self.pos[1]+i)
                if not board.get_square(position).occupying_piece:
                    legal_moves.append(position)
                elif board.get_square(position).occupying_piece.color != self.color:
                    legal_moves.append((position))
                    break
                else:
                    break

        return legal_moves
