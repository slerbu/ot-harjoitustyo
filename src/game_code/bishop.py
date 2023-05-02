import pygame
from game_code.piece import Piece


class Bishop(Piece):
    """
    Class representing a bishop chess piece
    Attributes:
        color: Color of bishop, "white" or "black"
        pos: Position on board
        board: The board where bishop is placed
        type: type of chess piece -> bishop
        image: image of bishop
        rect: rectangular area of bishop image

    """

    def __init__(self, color, position, board):
        super().__init__(color, position, board)
        self.type = "Bishop"
        self.image = pygame.image.load(
            f"src/game_code/imgs/{self.color}_{self.type.lower()}.png")
        self.image = pygame.transform.scale(
            self.image, (int(board.tile_width), int(board.tile_height)))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] * board.tile_width
        self.rect.y = self.pos[1] * board.tile_height

    def get_legal_moves(self, board):
        """
        Function to get a list of legal positions for bishop to move to on chess board

        Args:
            board: board to check positions on

        Returns:
            list of legal positions to move to
        """

        legal_moves = []
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
                legal_moves.append((self.pos[0]-i, self.pos[1]-i))
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
