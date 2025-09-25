from pico2d import *

#시작할때
#sprite L B W H
#speite = (((0,0,100,100),(100,0,100,100),(200,0,100,100)),#action 0
#        ((1,2,3,4),(1,2,3,4),(1,2,3,4)),#action 1
#      ((1,2,3,4),(1,2,3,4),(1,2,3,4)) )#action 2
# )
#
#def play_animation(action):
# for frame in action:
#  clear_canvas()
#  image.clip_draw(frame[0],frame[1],frame[2],frame[3],400,300)
#  update_canvas()
#  delay(0.1)
#
#while True:
# for action in sprite:
#  for i in range(5):
#   play_animation(action)
#  delay(1)
#
#

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


# fill here
running = True


def handle_events():
    # fill here
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    pass


frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    # fill here
    handle_events()
    if not running:
        break



    frame = (frame + 1) % 8
    delay(0.01)


close_canvas()
