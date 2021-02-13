import numpy as np
from items import *
from headerfile import *
import random

sys_random = random.SystemRandom()

class Bricks:
    """ This class handles all brick related functionality
    """
    def __init__(self):
        self.brick_start_x = 20
        self.brick_start_y = 45
        self.brick_configuration = brick_orientation[sys_random.randint(0,((brick_orientation.size)-1))].split()
    
    def update_brick_onscreen(self,screen_array):
        """ This function is used to update the value of bricks on the screen array
            Using Randomly picked brick orientation 
        """
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

    def remove_brick_onscreen(self,screen_array,x,y):
        """ This function is used to remove bricks that are being hit
        """
        pointer_1 = y
        pointer_2 = y
        flag = 0 
        if(screen_array[x][pointer_2][10]==']'):
            flag = 1
        while (screen_array[x][pointer_1][10]!='['):
            screen_array[x][pointer_1] = ' '
            pointer_1 -= 1
        screen_array[x][pointer_1] = ' '
        pointer_2 += 1
        if(not flag):
            while (screen_array[x][pointer_2][10]!=']'):
                screen_array[x][pointer_2] = ' '
                pointer_2 += 1
            screen_array[x][pointer_2] = ' '
