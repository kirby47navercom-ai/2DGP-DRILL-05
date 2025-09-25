from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def dir_check():
    global x,y,dirx, diry

    if dirx == 1 or dirx == -1:
        x += dirx * 10
        if 30 > x or x > 750:
            x -= dirx * 10
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    if diry == 1 or diry == -1:
        y += diry * 10
        if 30 > y or y> 550:
            y -= diry * 10
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    if dirx ==0 and diry == 0:
        character.clip_draw(frame * 100, 300, 100, 100, x, y)

def handle_events1():
    global dirx, diry
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1




x = 800 // 2
y = 180 // 2
frame = 0
dirx = 0
diry = 0




while True:
    clear_canvas()
    grass.draw(400, 100)

    handle_events1()
    dir_check()

    frame= (frame + 1) % 8
    update_canvas()
    delay(0.01)


close_canvas()