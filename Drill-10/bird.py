import game_framework
from pico2d import *

import game_world
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.font = load_font('ENCR10B.TTF',16)

        self.image = load_image('bird_animation.png')
        # fill here
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.framex = 0
        self.framey = 0

        self.num=0



    def add_event(self, event):
        pass
    def update(self):
        self.velocity=0
        if self.dir ==1:
            self.velocity += RUN_SPEED_PPS
        elif self.dir ==-1:
            self.velocity -= RUN_SPEED_PPS
        self.num += 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        self.x += self.velocity * game_framework.frame_time

        self.x = clamp(0, self.x, 1600)
        if self.x == 1600:
            self.dir =-1
        elif self.x == 0:
            self.dir = 1

        self.framex = int(self.frame) % 5
        if int(self.frame) % 12 == 0:
            self.framey = 2
        if int(self.frame) % 12 == 5:
            self.framey = 1
        if int(self.frame) % 12 == 10:
            self.framey = 0
        #print('frame : %d' % (self.frame % 14))
       # print('framex : %d' % (self.framex))
        #print('framey : %d' % (self.framey))
        print(RUN_SPEED_PPS)


        pass

    def draw(self):
        self.font.draw(self.x-60, self.y+50, '(Time: %3.2f)' %get_time(), (255,255,0))
        if self.dir == 1:
            self.image.clip_composite_draw(self.framex * 182, self.framey * 168, 183, 168,0, '', self.x, 300,100,100)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.framex * 182, self.framey * 168, 183, 168, 3.141592 , 'v', self.x, 300, 100,100)
        pass

    def handle_event(self, event):
        pass