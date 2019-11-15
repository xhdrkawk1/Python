import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from brick import Brick

name = "MainState"

boy = None
grass = None
brick = None
balls = []
big_balls = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global boy
    global brick
    brick = Brick()
    boy = Boy()
    game_world.add_object(boy, 1)
    game_world.add_object(brick, 1)
    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls
    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # fill here for collision check
    for ball in balls:
        if collide(brick, ball):
            if ball.x <= brick.x and ball.y <= brick.y + 21:
                ball.x = brick.x - 101
            elif ball.x >= brick.x and ball.y <= brick.y + 21:
                ball.x = brick.x + 101
            else:
                if ball.Init is False:
                    ball.Init = True
                    ball.TermX = ball.x - brick.x
                    ball.Coli = True
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)
    for ball in balls:
        if collide(grass, ball):
            ball.stop()
    if collide(grass, boy):
        boy.y = 95
    if collide(brick, boy):
        if boy.Init is False and boy.t > 0.5:
            boy.Init = True
            boy.Term = boy.x - brick.x
            boy.isColi = True
            boy.Initialize_Boy()
    else:
        boy.isColi = False


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
