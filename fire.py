from headerfile import *
from items import *

class fire:
    def __init__(self,x,y):
        self.cur_x = x
        self.cur_y = y
        self.initial_x = x
        self.initial_y = y
        self.alive = True
        self.ballcollide = False
        self.interactball = False

    def move(self,bricks_class):
        self.initial_x += -1
        self.initial_y += 0
        self.collide(bricks_class)

    def cur_returnxy(self):
        return (self.cur_x,self.cur_y)

    def initial_returnxy(self):
        return (self.initial_x,self.initial_y)

    def collide(self,bricks_class):
        if(self.cur_x <= 1):
            self.alive = False
        else:
            bricks = bricks_class.bd_return()
            for i in range(0,bricks.shape[0]):
                for j in range(0,bricks[0].size):
                    size = bricks[i][j].returnbsize()
                    (x,y) = bricks[i][j].returnxy()
                    if(self.cur_x == x and (self.cur_y >= y and cur_y <= y+size) and self.alive ):
                        temp = False
                        bricks.remove_brick_onscreen(screen_array,x,y,temp)
                        self.die()
    
    def die(self):
        self.alive = False
        return self.alive
