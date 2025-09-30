from pico2d import *


# fill here
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('animation_sheet.png')


def handle_events():
    global running

    # fill here
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
            #마우스는 윈도우 좌표계임
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False



running = True
frame = 0

# fill here
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()


while running:
    clear_canvas()

    # fill here
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.01)

close_canvas()




