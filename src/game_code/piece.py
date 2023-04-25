import pygame

class Piece:
    def __init__(self, color, position, board, type):
        self.color = color
        self.pos = position
        self.type = type
        self.board = board
        
        self.image = pygame.image.load(f"src/game_code/imgs/{self.color}_{self.type.lower()}.png")
        self.image = pygame.transform.scale(self.image, (int(board.tile_width), int(board.tile_height)))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] * board.tile_width
        self.rect.y = self.pos[1] * board.tile_height

    def draw(self, screen):
       
        screen.blit(self.image, self.rect)

    def move(self, new_pos):
        old_x, old_y = self.pos
        new_x, new_y = new_pos
        self.board.mapping[old_y][old_x] = "0"
        self.board.mapping[new_y][new_x] = f"{self.color[0]}{self.type[0]}"
        self.pos = new_pos
        print(self.pos)

        # self.legal_moves = self.get_legal_moves()
        print(new_pos)

    # def get_legal_moves(self):
    