import numpy as np
from headerfile import *
from paddle import *
from items import *

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
                self.active = 2
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
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
                self.active = 2
            else:
                if(y >= paddle_start and y <= paddle_end):
                    if(screen_array[self._x-1][self._y] == temp):
                    screen_array[self._x-1][self._y] == ' '
                    # update paddle size
                    Paddle.update_type(0)
            self._x += 1

# class paddle_grab(shrink_paddle):
#     def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
#         self.check_time()
#         if(self.active == 1):
#             if(x != 43):
#                 temp = powerup_temper[0]
#                 if(screen_array[self._x-1][self._y] == temp):
#                     screen_array[self._x-1][self._y] == ' '
#                 screen_array[self._x][self._y] = temp
#                 self.active = 2
#             else:
#                 if(y >= paddle_start and y <= paddle_end):
#                     if(screen_array[self._x-1][self._y] == temp):
#                     screen_array[self._x-1][self._y] == ' '
#                     # update paddle size
#                     Paddle.update_type(0)
#             self._x += 1