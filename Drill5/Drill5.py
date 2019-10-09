from pico2d import *
import math


KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global PosX, PosY
    global blsMove
    global MousePosX, MousePosY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            PosX = event.x
            PosY = KPU_HEIGHT - 1 - event.y
            blsMove = False

        elif event.type == SDL_MOUSEBUTTONDOWN:
            MousePosX = event.x
            MousePosY = KPU_HEIGHT - 1 - event.y
            blsMove = True

open_canvas(KPU_WIDTH, KPU_HEIGHT)
Kpu_ground = load_image('KPU_GROUND.png')
Player = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

running = True

PosX = KPU_WIDTH // 2
PosY = KPU_HEIGHT // 2

MousePosX = PosX
MousePosY = PosY

PlayerPosX = 100
PlayerPosY = 100
PlayerRight = False
frame = 0
blsMove = False
while running:
    clear_canvas()

    Kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    Mouse.draw(MousePosX, MousePosY)
    if PlayerRight == False:
     Player.clip_draw(frame * 100, 0, 100, 100, PlayerPosX, PlayerPosY)
    else:
     Player.clip_draw(frame * 100, 100, 100, 100, PlayerPosX, PlayerPosY)

    update_canvas()

    frame = (frame + 1) % 8

    delay(0.03)

    handle_events()

    if MousePosX > PlayerPosX and blsMove == True:
        PlayerRight = True
    elif MousePosX < PlayerPosX and blsMove == True:
        PlayerRight = False

    if blsMove == True:
        PlayerPosX += (MousePosX - PlayerPosX)*0.05
        PlayerPosY += (MousePosY - PlayerPosY)*0.05



