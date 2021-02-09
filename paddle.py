import numpy as np
from items import *
from headerfile import *

class paddle:
    def __init__(self,current_X,current_Y,current_type):
        self.cur_x = current_X
        self.cur_y = current_Y
        self.type = current_type

    def update_paddle_onscreen(self,screengrid):
        paddle_val = paddle_size[self.type]
        paddle = '<'
        for i in range(0,paddle_val):
            paddle = paddle + '='
        paddle = paddle + '>'
        size = len(paddle)
        half_size = (int)(size/2)
        start = self.cur_x - half_size
        end = self.cur_x + half_size + 1
        for i in range(start-1,end+1):
            screengrid[self.cur_y][i] = ' '
        j=0
        for i in range(start,end):
            screengrid[self.cur_y][i] = paddle[j]
            j+=1

    def update_paddle_value(self,changed_X,changed_Y,changed_type):
        self.cur_x = changed_X
        self.cur_y = changed_Y
        self.type = changed_type
