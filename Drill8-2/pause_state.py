import game_framework
from pico2d import *
import main_state
import title_state


name = "PauseState"
PauseBotton = None


class CPause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.blink = 0

    def draw(self):
        if self.blink == 0:
            self.image.draw(400, 300)

    def update(self):
        self.blink = (self.blink + 1) % 2


def enter():
    global PauseBotton
    PauseBotton = CPause()


def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    PauseBotton.draw()
    update_canvas()


def update():
    PauseBotton.update()
    delay(0.1)

def pause():
    pass


def resume():
    pass