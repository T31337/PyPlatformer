import pygame
from Level import *
from colors import *
from Block import *
from MyPlayer import *
class Level_01(Level):
    def __init__(self,Player_Object):
       
        #super(Level_01,self).__init__(Player_Object,(player_start))
        Level.__init__(self, Player_Object)
<<<<<<< HEAD
        self.player_start = self.player_startX,self.player_startY = 20,10
=======
        #self.player_start = self.player_startX,self.player_startY = 20,10
        self.player_start = 75,46
        
>>>>>>> a0556f7d31c4ff51534bc612a977030131524cd7
        level = [
        #[x,y,width,height,color]
        [15,124,365,10,purple],
        [300,30,600,10,green]
        ]
        
        for block in level:
            block = Block(block[0],block[1],block[2],block[3],block[4])
            self.object_list.add(block)