import pygame
from pygame.locals import *
from colors import *
from Level import *
class MyPlayer(pygame.sprite.Sprite):
    
    def __init__(self,width=32,height=48,color=green,Active_Object_List=[]):
        self.object_list = Active_Object_List
        super(MyPlayer,self).__init__()
        #pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.set_properties()
        self.hspeed = 0
        self.vspeed = 0
        self.level = None
        self.world_shift_x = 0
        self.world_shift_y = 0
        
        self.left_viewbox = 300 - 100#window_width/2 - window_width/8
        self.right_viewbox = 300 + 80#window_heigt/2+window_width/10
        self.up_viewbox = 10
        self.down_viewbox = 700
    def getLocation(self):
        return self.rect.centerx,self.rect.centery
   # def change_speed(self,hspeed,vspeed):
   #     self.hspeed+=hspeed
   #     self.vspeed+=vspeed
   
      
    def shift_world(self,shift_x,shift_y):
        self.world_shift_x += shift_x
        self.world_shift_y += shift_y
        for each_object in self.object_list:
            each_object.rect.x += shift_x
            each_object.rect.y += shift_y
          
    def scroll(self):
        if self.rect.x <= self.left_viewbox:
            viewdiff = self.left_viewbox - self.rect.x
            self.rect.x = self.left_viewbox
            self.shift_world(viewdiff,0)
        if self.rect.x <= self.right_viewbox:
            viewdiff = self.right_viewbox - self.rect.x
            self.rect.x = self.right_viewbox
            self.shift_world(viewdiff,0)
        if self.rect.y <= self.up_viewbox:
            viewdiff = self.up_viewbox - self.rect.y
            self.rect.y = self.down_viewbox
            self.shift_world(0,viewdiff)
        if self.rect.y <= self.down_viewbox:
            viewdiff = self.down_viewbox - self.rect.y
            self.rect.y = self.down_viewbox
            self.shift_world(0,viewdiff)           
    def set_properties(self):
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        self.speed = 5

    def set_position(self,x,y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_level(self,level):
        self.level = level
        self.set_position(level.player_startX, level.player_startY)
    
    def set_image(self,fileName = None):
        if fileName != None:
            self.image = pygame.image.load(fileName).convert_alpha()
            self.set_properties()
    
    def update(self,collidable = pygame.sprite.Group(),event = None):
        self.experience_gravity()
        self.rect.x += self.hspeed
        collision_list = pygame.sprite.spritecollide(self,collidable,False)
        for collided_object in collision_list:
            if self.hspeed > 0:
                self.rect.right = collided_object.rect.left
            elif self.hspeed < 0:
                self.rect.left = collided_object.rect.right
        self.rect.y += self.vspeed
        collision_list = pygame.sprite.spritecollide(self,collidable,False)
        for collided_object in collision_list:
            if self.vspeed > 0:
                self.rect.bottom = collided_object.rect.top
                self.vspeed = 0
            if self.vspeed < 0:
                self.rect.top = collided_object.rect.bottom
                self.vspeed = 0
        '''
        if not (event == None):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hspeed = -self.speed
                if event.key == pygame.K_RIGHT:
                    self.hspeed = self.speed
                if event.key == pygame.K_SPACE:
                    if len(collision_list) >=1:
                        self.vspeed = -(self.speed)*2
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if self.hspeed < 0:
                        self.hspeed = 0
                if event.key == pygame.K_RIGHT:
                    if self.hspeed > 0:
                        self.hspeed = 0
                        
            if event.type == MOUSEMOTION:
                mousePos = event.pos #pygame.mouse.get_pos()
                print('Mouse: '+str(mousePos[0])+','+str(mousePos[1]))        
            '''
        #if self.rect.y > 600:
            #print("You Died!")
    def experience_gravity(self,gravity = .35):
        if self.vspeed == 0:
            self.vspeed = 1
        else:
            self.vspeed += gravity