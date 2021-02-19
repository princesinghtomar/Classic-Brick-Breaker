import numpy as np
from headerfile import *
from paddle import *
from items import *
from ball import *
import time

# Active = 0 // not active or release
# Active = 1 // released but not yet taken by the player
# Active = 2 // taken by player

class power0:
    def __init__(self,time_activated,x,y):
        self.time_activated = time_activated
        self.active = 0
        self.max_time = 35
        self._x = x + 5
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

    def return_status(self):
        self.check_time()
        return self.active

    def update_powerup_onscreen(self,screen_array,paddle_end,paddle_start,Paddle):
        self.check_time()
        # print("helo")
        # print("1 : self._x : " + str(self._x) + " self._y : " + str(self._y))
        if(self.active == 1):
            if(self._x < 43):
                # print("2  : self._x : " + str(self._x) + " self._y : " + str(self._y))
                temp = powerup_temper[0]
                screen_array[self._x-1][self._y] = ' '
                screen_array[self._x][self._y] = temp
                # print("fucking hell ")
            elif(self._x > 43):
                # screen_array[self._x-2][self._y] = ' '
                self.active = 0
                # print("fuck")
            else:
                temp = powerup_temper[0]
                screen_array[self._x-1][self._y] = ' '
                if(self._y >= paddle_start and self._y <= paddle_end):
                    self.active = 2
                    # print("reached here : " + str(self.active))
                    return True
            self._x += 1