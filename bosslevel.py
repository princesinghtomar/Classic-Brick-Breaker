from headerfile import *
from art import art
import numpy as np
import random 
import time
import logging
from inherit_brick import *

class Boss:
    def __init__(self,py,score):
        self.py = py    #paddle y
        self.px = 7
        self.life = 100
        self.score = score
        self.sbricks = []
        self.pstart = 0
        self.pend = 0
        self.ufo = art.ufo.split('9')
        self.unb = [self.pstart + 10, self.pend - 20, len(self.ufo) + self.px]
        self.spawnbricks = [False,False]

    def cp(self):
        self.pstart = self.py - 22
        self.pend = self.py + 22
        if(self.pstart <= 2):
            self.pstart = 2
            self.pend = pstart + 44
        elif(self.pend >= WIDTH - 2):
            self.pend = WIDTH -2
            self.pstart = self.pend - 44
        self.unb = [self.pstart + 10, self.pend - 20, len(self.ufo) + self.px]

    def updatepy(self,py,screen_array):
        self.clear(screen_array)
        self.check_spawing()
        self.py = py
        self.draw(screen_array)

    def draw(self,screen_array):
        self.cp()
        self.bswfun(screen_array,True)
        for i in range(0,len(self.ufo)-1):
            for j in range(0,len(self.ufo[i])):
                screen_array[self.px+i][self.py + j] = self.ufo[i][j]

    def clear(self,screen_array):
        self.bswfun(screen_array,False)
        for i in range(0,len(self.ufo)-1):
            for j in range(0,len(self.ufo[i])):
                screen_array[self.px+i][self.py + j] = ' '

    def check_spawing(self):
        if(self.life <= 50 and self.life > 20 and not self.spawnbricks[0]):
            self.binit()
            self.spawnbricks[0] = True
        if(self.life <= 20 and not self.spawnbricks[1]):
            self.binit()
            self.spawnbricks[1] = True

    def decreaselife(self):
        self.life = self.life - 10
        self.score += 30

    def rlife(self):
        return self.life

    def collision(self,screen_array,x,y):
        if(x <= self.px ):
            self.decreaselife()
            return(self.score,80)
        else:
            for i in range(len(self.sbricks)):
                (x1,y1) = self.sbricks[i].returnxy()
                size = self.sbricks[i].returnbsize()
                if(x == x1 and (y >= y1 and y <= y1 + size)):
                    (life,typeb,score_) = self.sbricks[i].decrease_brick_life(1,False)
                    self.sbricks[i].clear(screen_array)
                    self.sbricks[i].draw(screen_array)
                    self.score += score_
                    return(score_,80)   # (score,choosen_value)
            logging.debug("x y : " + str((x,y)))
            return(0,0)

    def binit(self):
        if(not self.spawnbricks[0] and not self.spawnbricks[1]):
            if(len(self.sbricks) < 2):
                self.sbricks.append(Brick_inherit(self.unb[0],self.unb[2]))
                self.sbricks.append(Brick_inherit(self.unb[1],self.unb[2]))
        elif(self.spawnbricks[0] and not self.spawnbricks[1]):
            # if(len(self.sbricks) < 13):
            lamda = 0 
            for i in range(0,7):
                self.sbricks.append(Brick_inherit(0,self.px + len(self.ufo) + 1,self.pstart + lamda))
                lamda += self.sbricks[-1].returnbsize()
        elif(self.spawnbricks[0] and self.spawnbricks[1]):
            # if(len(self.sbricks) < 13):
            lamda = 0 
            for i in range(0,7):
                self.sbricks.append(Brick_inherit(1,self.px + len(self.ufo) + 2,self.pstart + lamda))
                lamda += self.sbricks[-1].returnbsize()

    # use : True, then draw otherwise clear
    def bswfun(self,screen_array,use):
        for i in range(len(self.sbricks)):
            if(self.sbricks[i].return_alive()):
                if(use):
                    self.sbricks[i].draw(screen_array)
                else:
                    self.sbricks[i].clear(screen_array)
