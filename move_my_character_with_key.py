from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
boy = load_image('boy.png')

def handle_events():
    global running, dir_x, dir_y, moving
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            moving = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            moving = False
running = True
x = 961 // 2
y = 832 // 2
frame = 0
dir_x = 0
dir_y = 0
moving = False
frame_idle = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if x < 0 or x > TUK_WIDTH or y < 0 or y > TUK_HEIGHT:
        exit(0)
    if moving:
        if dir_x > 0:
            boy.clip_draw(frame * 96, 0, 96, 107, x, y)
        elif dir_x < 0:
            boy.clip_draw(frame * 96, 208, 96, 103, x, y)
        if dir_y > 0:
            boy.clip_draw(frame * 96, 100, 96, 108, x, y)
        elif dir_y < 0:
            boy.clip_draw(frame * 96, 310, 96, 105, x, y)
    else:
        boy.clip_draw(frame_idle * 96, 720, 96, 107, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    frame_idle = (frame + 1) % 3
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()


