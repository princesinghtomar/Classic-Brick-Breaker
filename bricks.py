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
    def __init__(self,level):
        self.brick_start_x = 20
        self.brick_start_y = 45
        self.sys_random = random.SystemRandom()
        self.brick_configuration = brick_orientation[level-1].split()
        self.brick_data = np.array([])
        self.poweruparray = [0 for i in range(1,200)]
        self.starttime = time.time()
        self.previousfall = time.time()
        self.falldowngap = 0
        self.startinggap = 0
        self.level = level
        self.startfalling = False
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
        # logging.debug("self.level : "  + str(self.level))
        if(self.level == 3):
            return
        if(self.brick_data.size == 0):
            # logging.debug("In part \"if condition\" of update_brick_function")  #
            for i in range(0,bricks_splitted_array.size):
                splited_bricks = np.array(bricks_splitted_array[i].split('-'))
                lamda = self.brick_start_y
                brci_temp = []
                for k in range(0,splited_bricks.size):
                    brci_temp.insert(k,Brick_inherit(int(splited_bricks[k]),i+self.brick_start_x,lamda))
                    brci_temp[k].draw(screen_array)
                    lamda+=6
                temp_brick_data.append(brci_temp)
            self.brick_data = np.array(temp_brick_data)
            # logging.debug("self.brick_data : " + str(self.brick_data))  #
        else:
            # logging.debug("In part \"else condition\" of update_brick_function")    #
            a = [i for i in range(0,len(brick_life_store))]
            for i in range(0,self.brick_data.shape[0]):
                for j in  range(0,self.brick_data[0].size):
                    # logging.debug("i : " + str(i) + " : j : " + str(j) + "(life,typeb) : " + str((self.brick_data[i][j].return_some_debug_value())))
                    (x,y) = self.brick_data[i][j].returnxy()
                    if(self.brick_data[i][j].return_alive()):
                        temp = self.return_choice(a)
                        if(self.brick_data[i][j].retrainbow()):
                            self.brick_data[i][j].update_type(temp)
                        self.brick_data[i][j].draw(screen_array)
                    else:
                        self.brick_data[i][j].clear(screen_array)


    def remove_brick_onscreen(self,screen_array,x,y,go_thru):
        '''
        This function is used to remove bricks that are being hit
        '''
        os.system("aplay -q funstuff/stompenemy.wav")
        index= [0,0]
        for i in range(0,self.brick_data.shape[0]):
            index[0] = i
            for j in range(0,self.brick_data[0].size):
                index[1] = j
                # (x1,y1) == self.brick_data[i][j].returnxy()
                (x1,y1) = self.brick_data[i][j].returnxy()
                size = self.brick_data[i][j].returnbsize()
                if(x == x1 and (y >= y1 and y <= y1 + size)):   
                    break
            else:
                continue
            break
        # logging.debug("x1 : " + str(x1) + " : " + "y1 : " + str(y1))
        (life,typeb,score_) = self.brick_data[index[0]][index[1]].decrease_brick_life(1,go_thru)
        choosen_value = self.sys_random.choice(self.poweruparray)
        choosen_value = 3
        # logging.debug("self.brick_data[index[0]][index[1]].return_alive : " + str(self.brick_data[index[0]][index[1]].return_alive()))
        # logging.debug("(life,typeb,score_) : " + str((life,typeb,score_)))
        return (score_,choosen_value)

    def return_choice(self,a):
        return self.sys_random.choice(a)

    def mainfallbrickfunction(self,screen_array):
        if(self.startfalling):
            self.fallbrick(screen_array)
        else :
            self.check_falling()

    def fallbrick(self,screen_array):
        if(time.time() - self.previousfall > self.falldowngap):
            self.previousfall = time.time()
            if(len(self.brick_data)> 0 ):
                for i in range(0,self.brick_data.shape[0]):
                    for j in range(0,len(self.brick_data[0])):
                        self.brick_data[i][j].clear(screen_array)
                        self.brick_data[i][j].falldown()
    
    def check_falling(self):
        if((time.time() - self.starttime) > self.startinggap):
            self.startfalling = True

    def findlby(self):
        # logging.debug("I'm here")
        # logging.debug("self.brick_data.shape : " + str(self.brick_data.shape))
        if(self.brick_data.shape[0] == 0):
            # logging.debug("returned 1")
            return 1
        # logging.debug("Reached after return 1")
        i = self.brick_data.shape[0]-1
        j = len(self.brick_data[0])-1
        lowest = 0
        flag = 1
        while(i and flag):
            while(j and flag):
                if(self.brick_data[i][j].return_alive()):
                    (lowest,y) = self.brick_data[i][j].returnxy()
                    flag = 0
        return lowest

    def bkleft(self):
        brleft = 0
        for i in range(0,self.brick_data.shape[0]):
            for j in range(0,len(self.brick_data[0])):
                if(self.brick_data[i][j].return_alive()):
                    brleft += 1
        return brleft
        
    def killbs(self):
        for i in range(0,self.brick_data.shape[0]):
            for j in range(0,len(self.brick_data[0])):
                self.brick_data[i][j].die()
                # self.brick_data[i][j].clear()