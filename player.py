import pygame

class Rect_obj:
    def __init__(self,x,y,w,h,color,screen) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color 
        self.screen = screen
    def draw(self):
        obj = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0)
        return obj  
