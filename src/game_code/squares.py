import pygame

class Square:
    #Square class that allows handling of squares for chessboard
    def __init__(self, file, rank, width, height):
        self.width = width
        self.height = height
        #Coordinates
        self.file = file
        self.rank = rank
        # Position
        self.width_pos = rank*width
        self.height_pos = file*height
        self.pos = (rank,file)
        self.res_pos = (self.width_pos, self.height_pos)
        self.occupying_piece = None
        self.highlight = False
        #Square colors
        self.light_color = (255,255,255)
        self.highlight_color = (255, 0, 0)
        self.dark_color = (0,0,0)
        if (file + rank) % 2 == 0:
            self.color = "light"
        else:
            self.color = "dark"  
        self.tile = pygame.Rect(self.width_pos, self.height_pos, self.width, self.height)
    def draw(self, screen):
        if self.highlight:
            pygame.draw.rect(screen, self.highlight_color, (self.tile))
        elif self.color == "light":
            pygame.draw.rect(screen, self.light_color, (self.tile))
        else:
            pygame.draw.rect(screen, self.dark_color, (self.tile))
            
    