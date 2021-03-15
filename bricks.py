import numpy as np
from items import *
from headerfile import *
import random
from inherit_brick import *
import sys
from powerup import *
import logging

class Bricks:
    ''' 
    This class handles all brick related functionality
    '''
    def __init__(self):
        self.brick_start_x = 20
        self.brick_start_y = 45
        self.sys_random = random.SystemRandom()
        self.brick_configuration = brick_orientation[self.sys_random.randint(0,((brick_orientation.size)-1))].split()
        self.brick_data = np.array([])
        self.poweruparray = [0 for i in range(1,130)]
        for i in range(0,6):
            self.poweruparray[i] = 6-i

    def bd_return(self):
        return self.brick_data
    
    def update_brick_onscreen(self,screen_array):
        '''
        This function is used to update the value of bricks on the screen array
        using Randomly picked brick orientation 
        '''
        bricks_splitted_array = np.array(self.brick_configuration)
        lamda = 0
        temp_brick_data = []
        if(self.brick_data.size == 0):
            logging.debug("In part \"if condition\" of update_brick_function")  #
            for i in range(0,bricks_splitted_array.size):
                splited_bricks = np.array(bricks_splitted_array[i].split('-'))
                lamda = self.brick_start_y
                brci_temp = []
                for k in range(0,splited_bricks.size):
                    brci_temp.insert(k,Brick_inherit(int(splited_bricks[k]),i+self.brick_start_x,lamda))
                    for z in range(0,6):
                        temp = bricks_color[int(splited_bricks[k])] + bricks_font_color[int(splited_bricks[k])]
                        screen_array[i+self.brick_start_x][lamda] = temp +bricks[int(splited_bricks[k])][z] + all_reset
                        lamda+=1
                temp_brick_data.append(brci_temp)
            self.brick_data = np.array(temp_brick_data)
            logging.debug("self.brick_data : " + str(self.brick_data))  #
        else:
            logging.debug("In part \"else condition\" of update_brick_function")    #
            for i in range(0,self.brick_data.shape[0]):
                for j in  range(0,self.brick_data[0].size):
                    if(self.brick_data[i][j].return_alive):
                        (x,y) = self.brick_data[i][j].returnxy()
                        for z in range(0,self.brick_data[i][j].returnbsize()):
                            temp = bricks_color[self.brick_data[i][j].return_type()] + bricks_font_color[self.brick_data[i][j].return_type()]
                            screen_array[x][y+z] = temp +bricks[self.brick_data[i][j].return_type()][z] + all_reset

    def remove_brick_onscreen(self,screen_array,x,y,go_thru):
        '''
        This function is used to remove bricks that are being hit
        '''
        os.system("aplay -q funstuff/stompenemy.wav")
        pointer_1 = y
        if(screen_array[x][pointer_1][5]=='P'):
            return (0,0)
        while (screen_array[x][pointer_1][10]!='['):
            pointer_1 -= 1
            if(screen_array[x][pointer_1] == 'O' or screen_array[x][pointer_1] == ' '):
                if(len(screen_array[x][pointer_1-1])>2):
                    screen_array[x][pointer_1] = screen_array[x][pointer_1+1]
                    if(screen_array[x][pointer_1-1][10]== ']'):
                        break
                else:
                    i = pointer_1+1
                    while(screen_array[x][i][10]!=']' or screen_array[x][i][10]!='['):
                        if(screen_array[x][i][10]!=']'):
                            pointer_1 = i-5
                            break
                        elif(screen_array[x][i][10]!='['):
                            pointer_1 = i-6
                            break
                        i+=1
                        if(len(screen_array[x][i])<2):
                            break
                    else:
                        continue
                    break

        index= [0,0]
        for i in range(0,self.brick_data.shape[0]):
            index[0] = i
            for j in range(0,self.brick_data[i].size):
                index[1] = j
                if((x,pointer_1) == self.brick_data[i][j].returnxy()):
                    break
            else:
                continue
            break
        (life,typeb,score_) = self.brick_data[index[0]][index[1]].decrease_brick_life(1,go_thru)
        k_color = self.brick_data[index[0]][index[1]].change_color_brick(typeb)
        lamda = pointer_1
        if(life > 0):
            for z in range(0,6):
                    screen_array[x][lamda] = k_color +bricks[typeb][z] + all_reset
                    lamda+=1
        else:
            for z in range(0,6):
                    screen_array[x][lamda] = ' '
                    lamda+=1
        choosen_value = self.sys_random.choice(self.poweruparray)
        # choosen_value = 3
        return (score_,choosen_value)

