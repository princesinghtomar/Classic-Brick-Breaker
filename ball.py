import numpy as np
from items import *
from headerfile import *

class Ball:
    def __init__(self,velocity_x,velocity_y,x,y,screen_array):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self._x = x
        self._y = y
        if(screen_array[x][y] == ' '):
            screen_array[x][y] = 'O'
    # def update_ball_speed(self,velocity_x,velocity_y):
    #     self.velocity_x = velocity_x
    #     self.velocity_y = velocity_y

    def update_ball_motion(self,screen_array):
        temp_x = self._x + self.velocity_x
        temp_y = self._y + self.velocity_y
        previous_x = self._x
        previous_y = self._y
        a = screen_array[temp_x][temp_y]
        size = bricks.size
        array = [bricks_color[i]+bricks_font_color[i]+bricks[i][1]+all_reset for i in range(0,size)]
        screen_array[previous_x][previous_y] = ' '
        print(a)
        print(array[1])
        print(a == array[0] or a == array[1] or a == array[2] or a == array[3] )
        point_is = 1
        if(a == ' '):
            self._x = temp_x
            self._y = temp_y
        elif(a == bricks[0][0] or a == bricks[0][len(bricks[0])-1]):
            self.velocity_x = -self.velocity_x
        elif(a == array[0] or a == array[1] or a == array[2] or a == array[3] ):
            self.velocity_y = -self.velocity_y
        elif(a == '-' and (temp_y==0 or temp_x == 0)):
            self.velocity_y = -self.velocity_y
        elif(a == '|'):
            self.velocity_x = -self.velocity_x
        else:
            point_is = 0
        
        if(point_is):
            screen_array[self._x][self._y] = 'O'
            return 1
        else:
            return -2
        
    def update_ball_onscreen(self,screen_array):
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = 'O'

