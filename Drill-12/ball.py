import random

from pico2d import *

import game_world

import game_framework

import main_state



import boy

import zombie

class Ball:

    image = None

    def __init__(self):

        if Ball.image == None:

            Ball.image = load_image('ball21x21.png')

        self.x, self.y= random.randint(0, 1280-1), random.randint(300, 600-1)



    def get_bb(self):

        # fill here

        return self.x - 10, self.y - 10, self.x + 10, self.y + 10



    def draw(self):

        self.image.draw(self.x, self.y,20,20)

        # fill here for draw

        draw_rectangle(*self.get_bb())

    def update(self):

        pass

class BigBall:
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')

        self.x, self.y = random.randint(0, 1280 - 1), random.randint(300, 600 - 1)


    def get_bb(self):
        # fill here

        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)

        draw_rectangle(*self.get_bb())


    def update(self):
        pass