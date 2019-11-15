import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600 - 1), 60, 0
        self.Coli = False
        self.Brick = main_state.brick
        self.TermX = 0
        self.Init = False

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.Coli is False:
            self.y -= self.fall_speed * game_framework.frame_time

        if self.Coli is True and self.Init is True:
            self.x = self.Brick.x + self.TermX
            self.y = self.Brick.y + 40

    # fill here for def stop
    def stop(self):
        self.fall_speed = 0


# fill here
# class BigBall
class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(600, 1400 - 1), 500
        self.fall_speed = random.randint(100, 120)
        self.Coli = False
        self.Brick = main_state.brick
        self.Init = False

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20