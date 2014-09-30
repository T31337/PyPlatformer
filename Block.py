import pygame
from pygame.locals import *
from colors import *
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color=purple):
        super(Block,self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.origin_x = self.origin_x
        #self.origin_y = self.origin_y
        
    def set_properties(self):
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        self.speed = 5
    
    def setImage(self,fileName=None):
        if fileName !=None:
            self.image = pygame.image.load(fileName)
            