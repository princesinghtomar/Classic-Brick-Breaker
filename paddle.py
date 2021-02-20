import numpy as np
from items import *
from headerfile import *

# -- incr_dec_paddle
# if - 0 then No obtianed
# if - 1 then incr obtained
# if - 2 then dec obtained

class paddle:
    '''
    Handles paddle
    '''
    def __init__(self,current_X,current_Y,current_type):
        self.cur_x = current_X
        self.cur_y = current_Y
        self.type = current_type
        self.free_ball = False
        self.Stick_powerup = False
        self.incr_dec_paddle = 0

    def update_paddle_onscreen(self,screengrid):
        ''' 
        Focusses on updating paddle on screen
        '''
        paddle_val = paddle_size[self.type]
        paddle = '~'
        for i in range(0,paddle_val):
            paddle = paddle + '~'
        paddle = paddle + '~'
        size = len(paddle)
        half_size = int((paddle_size[self.type])/2)
        paddle_start = self.cur_x - half_size-1
        paddle_end = self.cur_x + half_size+1
        start_val = paddle_start-6 if paddle_start-6 < 1 else 1
        end_val = WIDTH-1 if paddle_end+6 > WIDTH-1 else paddle_end + 6
        for i in range(start_val,end_val):
            if(screengrid[self.cur_y][i]!='0' or screengrid[self.cur_y][i]!='|'):
                screengrid[self.cur_y][i] = ' '
        j=0
        for i in range(paddle_start,paddle_end):
            screengrid[self.cur_y][i] = paddle[j]
            j+=1
        screengrid[self.cur_y][0] = '|'
        screengrid[self.cur_y][WIDTH-1] = '|'
        

    def update_paddle_value(self,changed_X,changed_Y,changed_type):
        ''' 
        For updating paddle value in the class
        '''
        self.cur_x = changed_X
        self.cur_y = changed_Y
        self.type = changed_type

    def update_type(self,changed_type):
        '''
        Updates type of paddle used for powerup implementation
        '''
        self.type = changed_type

    def return_xandy(self):
        '''
        Return : (self.cur_x,self.cur_y)
        '''
        return (self.cur_x,self.cur_y)
