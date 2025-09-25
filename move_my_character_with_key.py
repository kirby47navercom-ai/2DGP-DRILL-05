from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def dir_check(check):
    global x,y

    if check == 0:
        character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif check == 1 or check == -1:
        x += dir * 5
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif check == 2 or check == -2:
        y += dir * 5
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

def handle_events1():
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1



x = 800 // 2
y = 180 // 2
frame = 0
dir = 0




while True:
    clear_canvas()
    grass.draw(400, 100)

    handle_events1()
    dir_check(dir)

    frame= (frame + 1) % 8
    update_canvas()
    delay(0.01)


close_canvas()