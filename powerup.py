import numpy as np
from headerfile import *
from paddle import *
from items import *
from ball import *

# Active = 0 // not active or release
# Active = 1 // released but not yet taken by the player
# Active = 2 // taken by player

class expand_paddle:
    def __init__(self,time_activated,x,y):
        self.time_activated = time_activated
        self.active = 0
        self.max_time = 35
        self._x = x
        self._y = y

    def update_time_activated(self):
        return self.time_activated

    def make_powerup_active(self):
        self.time_activated = time.time()
        self.active = 1

    def check_time(self):
        if(self.active != 0):
            if(time.time() - self.time_activated > self.max_time):
                self.active = 0

    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
        self.check_time()
        if(self.active == 1):
            if(x != 43):
                temp = powerup_temper[0]
                if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                screen_array[self._x][self._y] = temp
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                    self.active = 2
                    # update paddle size
                    Paddle.update_type(2)
            self._x += 1

class shrink_paddle(expand_paddle):
    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
        self.check_time()
        if(self.active == 1):
            if(x != 43):
                temp = powerup_temper[0]
                if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                screen_array[self._x][self._y] = temp
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                    self.active = 2
                    # update paddle size
                    Paddle.update_type(0)
            self._x += 1

class ball_multiplier(shrink_paddle):
    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,paddle,current_ball):
        self.check_time()
        ball_multiplier_flag = 0
        if(self.active == 1):
            if(x != 43):
                temp = powerup_temper[0]
                if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                screen_array[self._x][self._y] = temp
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                    self.active = 2
                    # here add return another ball :
                    ball_multiplier_flag = 1
            self._x += 1
        if(ball_multiplier_flag):
            curr_value = ball.return_class_init()
            if(screen_array[curr_value[2]][curr_value[3]]=='0'):
                another_ball = Ball(-curr_value[0],curr_value[1],curr_value[2],curr_value[3],screen_array)
                return another_ball
    return 0

class Fast_ball(shrink_paddle):
    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle,current_ball):
        self.check_time()
        if(self.active == 1):
            if(x != 43):
                temp = powerup_temper[0]
                if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                screen_array[self._x][self._y] = temp
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                    self.active = 2
                    # update ball speed
                    current_ball.update_speed()
            self._x += 1

class Thru_ball(shrink_paddle):
    def check_time(self,current_ball):
        if(self.active != 0):
            if(time.time() - self.time_activated > self.max_time):
                self.active = 0
                current_ball.


    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle,current_ball):
        self.check_time(current_ball)
        if(self.active == 1):
            if(x != 43):
                temp = powerup_temper[0]
                if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                screen_array[self._x][self._y] = temp
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                    self.active = 2
                    # update ball speed
                    current_ball.update_speed()
            self._x += 1
            
class Sticky_ball(shrink_paddle):
    