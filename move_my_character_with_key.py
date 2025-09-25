from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


x = 800 // 2
frame = 0
dir = 0
while True:
    clear_canvas()
    grass.draw(400, 100)
    update_canvas()
    delay(0.01)


close_canvas()