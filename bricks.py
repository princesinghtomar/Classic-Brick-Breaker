import numpy as np
from items import *
from headerfile import *
import random

random.seed(0)

class Bricks:
    def __init__(self):
        self.brick_start_x = 20
        self.brick_start_y = 45
        self.brick_configuration = brick_orientation[random.randint(0,((brick_orientation.size)-1))].split()
    
    def update_brick_onscreen(self,screen_array):
        bricks_splitted_array = np.array(self.brick_configuration)
        lamda = 0
        for i in range(0,bricks_splitted_array.size):
            for j in range(0,len(bricks_splitted_array[i])):
                splited_bricks = np.array(bricks_splitted_array[i].split('-'))
                lamda = self.brick_start_y
                for k in range(0,splited_bricks.size):
                    for z in range(0,6):
                        temp = bricks_color[int(splited_bricks[k])] + bricks_font_color[int(splited_bricks[k])]
                        screen_array[i+self.brick_start_x][lamda] = temp +bricks[int(splited_bricks[k])][z] + all_reset
                        lamda+=1