import pygame
from colors import *

class Level(object):
    
    def __init__(self,player_object):
        self.object_list = pygame.sprite.Group()
        self.player_object = player_object
        player_start = self.player_startX,self.player_startY = 0,0
        
    def update(self):
        self.object_list.update()
        
    def draw(self,window):
        window.fill(white)
        self.object_list.draw(window)
        