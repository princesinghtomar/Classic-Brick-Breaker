from headerfile import *
import numpy as np

class gametop:
    def __init__(self,timeleft,score,livesleft):
        self.timeleft = int(timeleft)
        self.score = score
        self.livesleft = livesleft

    def update_gametop(self,timeleft,score,livesleft):
        self.timeleft = timeleft
        self.score = score
        self.livesleft = livesleft
    
    def update_gametop_onscreen(self,screen_array):
        string = np.array(["Time  : " + str(round(self.timeleft))+ '   ',"Lives : " + str(self.livesleft) + '   ',"Score : " + str(self.score) + '   '])
        for i in range(0,len(string)):
            for j in range(0,len(string[i])):
                screen_array[i+1][j+4] = string[i][j]
