from pico2d import *
import math


KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global Posx, Posy
    global MouseposX, MousePosY
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            Posx = event.x
            Posy = KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            MouseposX = event.x
            MouseposY =KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False