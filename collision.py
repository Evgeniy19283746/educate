import pygame as pg
import sys


pg.init()

fps = 120
windiw_widht = 600
windiw_height = 400

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

r = 50
widht_rect = 150
height_rect = 100

widht_rect1 = 150
height_rect1 = 100


x, y = 400, 200
direct_x = 1
direct_y = 1

x1, y1 = 200, 200
direct_x1 = 1
direct_y1 = 1

x_rect = windiw_widht // 2 - widht_rect // 2
y_rect = windiw_height // 2 - height_rect // 2

x_rect1 = (windiw_widht // 2 - widht_rect // 2) + 160
y_rect1 = windiw_height // 2 - height_rect // 2

count_of_collision = 0

screen = pg.display.set_mode((windiw_widht, windiw_height))
clock = pg.time.Clock()

"""управление с клавы"""
run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            """запись количества столкновений"""
            with open('count_of_collision1.txt', 'w', encoding='utf-8') as score:
                score.write(f'Колличесто столкновений: {count_of_collision}')
            sys.exit()
#         elif i.type == pg.KEYDOWN:
#             if i.key == pg.K_LEFT:
#                 x_rect += -direct_x
#             elif i.key == pg.K_RIGHT:
#                 x_rect += direct_x
#             elif i.key == pg.K_UP:
#                 y_rect += -direct_y
#             elif i.key == pg.K_DOWN:
#                 y_rect += direct_y
    clock.tick(fps)
    screen.fill(white)

# ball_1 = pg.draw.circle(screen, red, (x, y), r)
# ball_2 = pg.draw.circle(screen, black, (x1, y1), r)
    """ столкновение прямоугольников по оси x"""
    pg.draw.rect(screen, red,
                     (x_rect, y_rect, widht_rect, height_rect)
                     )

    pg.draw.rect(screen, black,
                     (x_rect1, y_rect1, widht_rect, height_rect)
                     )

    x_rect += direct_x
    if x_rect >= windiw_widht - widht_rect or x_rect < 0:
            direct_x = -direct_x

    x_rect1 += -direct_x1
    if x_rect1 >= windiw_widht - widht_rect1 or x_rect1 < 0:
            direct_x1 = -direct_x1

    if x_rect + widht_rect == x_rect1:
            direct_x = -direct_x
            direct_x1 = -direct_x1
            count_of_collision += 1
            print(f'количество столкновений: {count_of_collision}')

    """перемещение с клавиатуры"""
# pg.draw.rect(screen, red,
#              (x_rect, y_rect, widht_rect, height_rect)
#              )

    pg.display.update()
