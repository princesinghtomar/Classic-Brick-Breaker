import numpy as np
from headerfile import *
from paddle import *
from items import *
from ball import *
import time
import logging

# Active = 0 // not active or release
# Active = 1 // released but not yet taken by the player
# Active = 2 // taken by player

class powerupclass:
    '''
    Main Powerup Class to handle motion and time of any powerup
    do : Used for activating Power Function
    undo : Used for deactivating Power Function
    '''
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

    def deactivate_time(self):
        self.time_activated = time.time() - self.max_time

    def update_xy(self,x,y):
        self.ballx = x + 5
        self.bally = y

    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
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
    '''
    Expand Paddle Powerup : Increases the size of the paddle 
    by a certain amount.
    '''
    def __init__(self,x,y,changed_type = 2):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 0

    def do(self,Paddle):
        Paddle.update_type(changed_type)
    
    def undo(self,Paddle):
        Paddle.update_type(1)

class power1(powerupclass):
    '''
    Shrink Paddle Powerup : Reduce the size of the paddle by a 
    certain amount but not completely.
    '''
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
    '''
    Ball Multiplier Powerup : Each of the balls which are present 
    will be further divided into two.
    '''
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 2

    def do(self,ball_class,screen_array):
        total_balls = len(ball_class)
        temp = []
        self.update_time_activated()
        for i in range(0,total_balls):
            (bavx,bavy,bax,bay) = ball_class[i].return_class_init()
            screen_array[bax][bay] = 'O'
            ball_class.append(Ball(bavx,-bavy,bax,bay,screen_array))
        logging.debug("do balls : "+ str(ball_class))

    def undo(self,ball_class,screen_array):
        for i in range(0,len(ball_class)-1):
            (bavx,bavy,bax,bay) = ball_class[i].return_class_init()
            screen_array[bax][bay] = ' '
            ball_class.pop(1)
        logging.debug("undo balls : "+ str(ball_class))

class power3(powerupclass):
    '''
    Fast Ball Powerup : Increases the speed of the ball.
    '''
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 3
        self.vx = 0
        self.vy = 0

    def do(self,ball_class):
        # for i in ball_class:
        #     i.increase_speed(2,2)   for multiple balls
        (bavx,bavy,bax,bay) = ball_class.return_class_init()
        self.vx = bavx
        self.vy = bavy
        ball_class.increase_speed(2,2)

    def undo(self,ball_class):
        # for i in ball_class:
        #     i.increase_speed(-2,-2)   for multiple balls
        ball_class.update_speed(-1,-1)

class power4(powerupclass):
    '''
    Thru-ball Powerup : This enables the ball to destroy and go through 
    any brick it touches, irrespective of the strength of the wall.
    '''
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
    '''
    Paddle Grab Powerup : Allows the paddle to grab the ball on contact and relaunch 
    the ball at will. The ball will follow the same expected trajectory after release, 
    similar to the movement expected without the grab.
    '''
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 5

    def do(self):
        return True

    def undo(self):
        return False

class power6(powerupclass):
    '''
    Powerup Class for Shooting paddle
    '''
    def __init__(self,x,y):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.ballx = x + 5
        self.bally = y
        self.index = 6
        self.shooting_gap = 0.2
        self.last_shot = 0
        self.power0 = None

    def do(self,Paddle):
        if(self.last_shot - time.time() > self.shooting_gap):
            if(self.last_shot == 0):
                self.last_shot = time.time()
                changed_type = Paddle.return_type + 3
                self.power0 = power0(Paddle,changed_type)
                self.power0.do(changed_type)
            else:
                self.power0.do(changed_type)
                
                # see tomorrow

