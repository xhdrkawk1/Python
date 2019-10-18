from pico2d import *
import random

# Game object class here


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw_object(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update_object(self):
        self.frame = (self.frame + 1) % 8
        self.x += 4

    def draw_object(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x = random.randint(10, 780)
        self.y = 700
        self.size = random.randint(0, 1)
        self.speed = random.randint(8, 20)
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update_object(self):
        if self.size == 0:
            if self.y <= 64:
                self.y = 64
            else:
                self.y -= self.speed
        elif self.size == 1:
            if self.y <= 74:
                self.y = 74
            else:
                self.y -= self.speed

    def draw_object(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code


open_canvas()

team = [Boy() for i in range(11)]
balls = [Ball() for j in range(20)]
grass = Grass()

running = True

# game main loop code


while running:
    handle_events()

    for boy in team:
        boy.update_object()

    for ball in balls:
        ball.update_object()

    clear_canvas()

    grass.draw_object()

    for boy in team:
        boy.draw_object()

    for ball in balls:
        ball.draw_object()

    update_canvas()

    delay(0.05)


# finalization code


close_canvas()
