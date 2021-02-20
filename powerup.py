import numpy as np
from headerfile import *
from paddle import *
from items import *
from ball import *
import time

# Active = 0 // not active or release
# Active = 1 // released but not yet taken by the player
# Active = 2 // taken by player

class powerupclass:
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 0

    def update_time_activated(self):
        self.time_activated = time.time()
        self.active = 2

    def make_powerup_active(self):
        self.time_activated = time.time()
        self.active = 1

    def check_time(self):
        val = True
        if(self.active != 0):
            if(time.time() - self.time_activated > self.max_time):
                self.active = 0
                val = False
        else:
            val = False
        return val

    def return_status(self):
        return self.active

    def update_status(self,st):
        self.active = st

    def update_xy(self,x,y):
        self.ballx = x + 5
        self.bally = y

    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
        #self.check_time()
        if(self.active == 1):
            if(self.ballx < 43):
                temp = powerup_temper[self.index]
                screen_array[self.ballx-1][self.bally] = ' '
                screen_array[self.ballx][self.bally] = temp
            elif(self.ballx > 43):
                self.active = 0
            else:
                temp = powerup_temper[self.index]
                screen_array[self.ballx-1][self.bally] = ' '
                if(self.bally >= paddle_start and self.bally <= paddle_end):
                    self.active = 2
                    return True
            self.ballx += 1
            return False

class power0(powerupclass):

    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 0

    def do(self,Paddle):
        Paddle.update_type(2)
    
    def undo(self,Paddle):
        Paddle.update_type(1)

class power1(powerupclass):
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 1

    def do(self,Paddle):
        Paddle.update_type(0)
    
    def undo(self,Paddle):
        Paddle.update_type(1)
    
class power2(powerupclass):
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 2

    def do(self,ball_class,screen_array,balls,ball_index):
        x = ball_class
        total_balls = len(ball_class)
        # temp = []
        # for i in range(0,total_balls):
        #     (bavx,bavy,bax,bay) = self.ball_class[i].return_class_init()
        #     ball_class.append(Ball(bavy,bavx,bax,bay,screen_array))
        #     temp.append(i)
        # balls.append(temp)
        # totla_balls = len(ball_index)
        # ball_index.append(totla_balls)
        #do nothing now

    def undo(self,ball_class,screen_array,ball_index):
        x = ball_class
        # index = ball_index[0]
        # for i in index:
        #     ball_class[i] = ""
        # index.pop(0)
        #undo nothing now

class power3(powerupclass):
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 3

    def do(self,ball_class):
        # for i in ball_class:
        #     i.increase_speed(2,2)   for multiple balls

        ball_class.increase_speed(-2,-2)

    def undo(self,ball_class):
        # for i in ball_class:
        #     i.increase_speed(-2,-2)   for multiple balls
        ball_class.increase_speed(-2,-2)

class power4(powerupclass):
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 4

    def do(self,ball_class):
        ball_class.update_thru_ball(True)

    def undo(self,ball_class):
        ball_class.update_thru_ball(False)

class power5(powerupclass):
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 5

    def do(self):
        # print("yup Reaced here")
        # sticky_ball_powerup = True
        return True

    def undo(self):
        # sticky_ball_powerup = False
        return False