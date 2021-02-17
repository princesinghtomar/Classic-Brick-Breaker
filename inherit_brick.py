import numpy as np
from items import *
from headerfile import *
import random

sys_random = random.SystemRandom()

#   ^ (-x)
#   |
#   |
#   -----> (+y)

class Brick_inherit:
    def __init__(self,typeb,starting_x,starting_y):
        self.type = typeb
        self.life = brick_life_store[typeb]
        self.color = bricks_color[typeb]+bricks_font_color[typeb]
        self.s_x = starting_x
        self.s_y = starting_y
        
    def decrease_brick_life(self,value,go_thru):
        if(go_thru):
            self.type = -1
            self.life = 0
        elif(self.type  != 3):
            self.life = brick_life_store[self.type]
            self.type -= 1
            return (self.life,self.type)
        return (self.life,self.type)
    
    def change_color_brick(self,typeb):
        self.color  = bricks_color[typeb]+bricks_font_color[typeb]
        return self.color

    def returnxy(self):
        return (self.s_x,self.s_y)
