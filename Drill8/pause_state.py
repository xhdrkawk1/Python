import game_framework
from pico2d import *
import main_state


name = "PauseState"
PauseBotton = None


class CPauseButton:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)


def enter():
   global  PauseBotton
   PauseBotton = CPauseButton()

def exit():
   pass


def handle_events():
    events = get_events()
    for event in events:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
def draw():
    clear_canvas()
    PauseBotton.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass