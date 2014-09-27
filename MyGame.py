#!/usr/bin/env python3
import pygame,sys

from colors import *
from MyPlayer import *
from Level import *
from Level_01 import *

class MyGame:
        
        pygame.init()
        
        def shift_world(self,shift_x,shift_y):
                self.world_shift_x += shift_x
                self.world_shift_y += shift_y
                for each_object in self.active_object_list:#for each_object in MyGame.collideable_objects:
                        each_object.rect.x += shift_x
                        each_object.rect.y += shift_y        
        def DeathEvent(self):
        
                MyFont = pygame.font.Font(None, 70)
                MyFont2 = pygame.font.Font(None, 50)
                self.rendered = MyFont.render(':( You Have Died!', True, red)
                self.rendered2 = MyFont2.render('Press R To Retry, Or Q/ESC To Quit!', True, (200,0,200))
                pygame.display.get_surface().fill(blue)  
                pygame.display.get_surface().blit(self.rendered,(125,225))
                pygame.display.get_surface().blit(self.rendered2,(70,300))                
                clock.tick(fps)
        def PlayMyGame(self):
                clock = pygame.time.Clock()
                fps = 60                
                sound = pygame.mixer.Sound('sounds/MarioClear.wav')
                #sound.play()
                window_size = window_width,window_height=800,600
                window = pygame.display.set_mode((800,600),pygame.DOUBLEBUF)
                pygame.display.set_caption("Epic Platformer!")
                running = True
                       
                
                MySurface = pygame.Surface((68,68))
                self.collideable_objects = pygame.sprite.Group()
        
                #Luigi.set_image('images/Luigi1.png')
                #Luigi.set_position(10,10)
                #Luigi.update()
                font = pygame.font.Font(None,100)
                text = font.render('Epic Platformer!', True, purple)
                self.active_object_list = pygame.sprite.Group()

                player = MyPlayer(Active_Object_List=self.collideable_objects)                         
                #self.active_object_list.add(player) 
                              
                player.set_image('images/Luigi1.png')
                player.set_position(25,17)
                self.active_object_list.add(player)
                block = Block(27, 500, width=500, height=7)
               
                window.fill(blue)
                
                level_list =  []
                level_list.append(Level_01(player))
                current_level_number = 0
                current_level = level_list[current_level_number]
                player.set_level(current_level)
                player.set_image('images/Luigi1.png')
                self.collideable_objects.add(self.active_object_list)
                
        
                while running:
                        for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                        running=False
                                if event.type==pygame.MOUSEMOTION:
                                        mousePos = event.pos #pygame.mouse.get_pos()
                                        print('Mouse@: '+str(mousePos[0])+','+str(mousePos[1]))        
                                if event.type==pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                                pygame.quit()
                                                sys.exit()
                                        if event.key == pygame.K_LEFT:
                                                player.hspeed-=5
                                        
                                        if event.key == pygame.K_RIGHT:
                                                player.hspeed+=5
                                        if event.key == pygame.K_SPACE:
                                                player.vspeed=(player.vspeed-5)*2
                                        print(str(event.key))
                                if event.type == MOUSEBUTTONDOWN:
                                        mousePos = event.pos
                                        player.set_position(mousePos[0],mousePos[1])
                                        player.update()
                        #update functions
                        player.update(current_level.object_list,event)
                        event = None
                        current_level.update()
                        player.scroll()
                        #logic testing
                        
                        #draw everyhing
                        current_level.draw(window)
                        self.active_object_list.draw(window)
                        #Limit FrameRate
                        clock = pygame.time.Clock()
                        clock.tick(60)
                        #update screen
                        pygame.display.update()
                        
                pygame.quit()
                sys.exit()
game = MyGame()
game.PlayMyGame()