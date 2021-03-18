import numpy as np
from headerfile import *
from paddle import *
from items import *
from ball import *
import time
import logging
from fire import *

# Active = 0 // not active or release
# Active = 1 // released but not yet taken by the player
# Active = 2 // taken by player

class powerupclass:
    '''
    Main Powerup Class to handle motion and time of any powerup
    do : Used for activating Power Function
    undo : Used for deactivating Power Function
    '''
    def __init__(self,x,y,vx,vy):
        self.time_activated = time.time()
        self.active = 0
        self.max_time = 15
        self.px = x
        self.py = y
        self.ball_initial = [x,y]
        self.index = 0
        self.interactball = False
        self.vx = vx
        self.vy = vy

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
        self.px = x
        self.py = y
        self.ball_initial =[x,y]
    
    def uballv(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def pdraw(self,screen_array,flag):
        temp = powerup_temper[self.index]
        logging.debug("self.py : " + str(self.py) + " : " + "self.px : " + str(self.px))
        if(not flag):
            screen_array[self.px][self.py] = ' '
        else:
            screen_array[self.px][self.py] = temp

    def ccoll(self):
        if(self.px <= 5):
            self.vx = -self.vx
            temp_val = 5 - self.px
            self.px = 5 + temp_val
            if(self.py <= 2):
                self.vy = -self.vy
                temp_val = 2 - self.py
                self.py = 2 + temp_val
            elif(self.py >= WIDTH-2):
                self.vy = -self.vy
                temp_val = (WIDTH - 2) - self.py
                self.py = (WIDTH - 2) + temp_val
            self.ball_x = self.px
            self.bal_y = self.py
        elif(self.py <=2 ):
            self.vy = -self.vy
            temp_val = 2 - self.py
            self.py = 2 + temp_val
        elif(self.py >= (WIDTH-2)):
            self.vy = -self.vy
            temp_val = (WIDTH - 2) - self.py
            self.py = (WIDTH - 2) + temp_val

    def pmove(self):
        t = time.time() - self.time_activated
        logging.debug("Before : self.py : " + str(self.py) + " : " + "self.px : " + str(self.px))
        self.px = int(self.ball_initial[0] + self.vx*t + (1/2)*10*(t**2))
        self.py = int(self.ball_initial[1] + self.vy*t)
        logging.debug("self.ball_initial : " + str(self.ball_initial))
        logging.debug("self.vy : " + str(self.vy) + " : " + "self.vx : " + str(self.vx))
        logging.debug("After : self.py : " + str(self.py) + " : " + "self.px : " + str(self.px))
        self.ccoll()

    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
        if(self.active == 1):
            self.pdraw(screen_array,False)
            self.pmove()
            logging.debug("After : self.py : " + str(self.py) + " : " + "self.px : " + str(self.px))
            if(self.px < 43):
                self.pdraw(screen_array,True)
            elif(self.px > 43):
                self.active = 0
            else:
                temp = powerup_temper[self.index]
                self.pdraw(screen_array,False)
                if(self.py >= paddle_start and self.py <= paddle_end):
                    self.active = 2
                    return True
            return False

class power0(powerupclass):
    '''
    Expand Paddle Powerup : Increases the size of the paddle 
    by a certain amount.
    '''
    def __init__(self,x,y,vx,vy,changed_type = 2):
        powerupclass.__init__(self,x,y,vx,vy)

    def do(self,Paddle):
        Paddle.update_type(changed_type)
    
    def undo(self,Paddle):
        Paddle.update_type(1)

class power1(powerupclass):
    '''
    Shrink Paddle Powerup : Reduce the size of the paddle by a 
    certain amount but not completely.
    '''
    def __init__(self,x,y,vx,vy):
        powerupclass.__init__(self,x,y,vx,vy)
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
    def __init__(self,x,y,vx,vy):
        powerupclass.__init__(self,x,y,vx,vy)
        self.index = 2

    def do(self,ball_class,screen_array):
        total_balls = len(ball_class)
        temp = []
        self.update_time_activated()
        for i in range(0,total_balls):
            (bavx,bavy,bax,bay) = ball_class[i].return_class_init()
            screen_array[bax][bay] = 'O'
            ball_class.append(Ball(bavx,-bavy,bax,bay,screen_array))
        # logging.debug("do balls : "+ str(ball_class))

    def undo(self,ball_class,screen_array):
        for i in range(0,len(ball_class)-1):
            (bavx,bavy,bax,bay) = ball_class[i].return_class_init()
            screen_array[bax][bay] = ' '
            ball_class.pop(1)
        # logging.debug("undo balls : "+ str(ball_class))

class power3(powerupclass):
    '''
    Fast Ball Powerup : Increases the speed of the ball.
    '''
    def __init__(self,x,y,vx,vy):
        powerupclass.__init__(self,x,y,vx,vy)
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
    def __init__(self,x,y,vx,vy):
        powerupclass.__init__(self,x,y,vx,vy)
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
    def __init__(self,x,y,vx,vy):
        powerupclass.__init__(self,x,y,vx,vy)
        self.index = 5

    def do(self):
        return True

    def undo(self):
        return False

class power6(powerupclass):
    '''
    Powerup Class for Shooting paddle
    '''
    def __init__(self,x,y,vx,vy):
        powerupclass.__init__(self,x,y,vx,vy)
        self.index = 6
        self.shooting_gap = 0.2
        self.last_shot = 0
        self.power0 = None
        self.changed_type = 2
        self.fire = [] 

    def do(self,Paddle):
        if(self.last_shot - time.time() > self.shooting_gap):
            if(self.last_shot == 0):
                self.last_shot = time.time()
                self.changed_type = Paddle.return_type + 3
                self.power0 = power0(Paddle,self.changed_type)
                self.power0.do(self.changed_type)
            else:
                self.power0.do(self.changed_type)

                fire.append()
                
                # see tomorrow

    def undo(self,Paddle):
        self.power0.undo()
