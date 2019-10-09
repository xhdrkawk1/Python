from pico2d import *
open_canvas()
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
def handle_events():
    global running
    global dir
    global diry
    global flag
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                flag = True
                if dir < 0:
                    dir = 0
                dir += 1
            elif event.key == SDLK_LEFT:
                flag = False
                if dir > 0:
                    dir = 0
                dir += -1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1

        elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    flag = True
                    if dir > 0:
                        dir = 0
                    dir += 1
                elif event.key == SDLK_LEFT:
                    if dir < 0:
                        dir = 0
                    flag = False
                    dir += -1
                elif event.key == SDLK_UP:
                    diry +=1
                elif event.key == SDLK_DOWN:
                    diry -= 1
        else :
          dir=0



x = 0
y=90
frame = 0
flag = True
dir = 0
diry = 0
while True:
    clear_canvas()
    grass.draw(400, 30)

    if flag == True:
     character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
     character.clip_draw(frame * 100, 0, 100, 100, x, y)

    x += dir*2
    y += diry*2

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    get_events()

    handle_events()

    if x > 800 :
     x=800
    elif x<0 :
     x=0
close_canvas()
