import pygame

class Square:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        #Coordinates
        self.x = x
        self.y = y
        # Positiom
        self.actual_x = x*width
        self.actual_y = y*height
        self.pos = (x,y)
        self.res_pos = (self.actual_x, self.actual_y)
        #Square colors
        if (x + y) % 2 == 0:
            self.color = "light"
            self.square_color = (255,255,255)
        else:
            self.color = "dark"
            self.square_color = (0,0,0)
        self.sq = pygame.Rect(self.actual_x, self.actual_y, self.width, self.height)
        
            


