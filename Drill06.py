from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running, mouse_x, mouse_y, points, point_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
            points.append((x, y))
            point_count += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def stamp_point():
    for i in range(start_point, len(points)):
        hand_arrow.draw(points[i][0], points[i][1])


running = True
x, y = 0, 0
mouse_x, mouse_y = 0, 0
start_x, start_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
end_x, end_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
points = []
point_count = 0
start_point = 0
frame = 0
index = 0
i = 0
frame_speed = 0
direction = 1

hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(mouse_x, mouse_y)
    stamp_point()
    update_canvas()
    handle_events()

close_canvas()