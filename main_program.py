import pygame as pg
from pygame.locals import *
import sys 

def create_floor():
    window.blit(floor,(floor_x_pos, 650))
    window.blit(floor,(floor_x_pos + 500,650))

width = 500
height = 750

pg.init()
window = pg.display.set_mode((width, height))
watch = pg.time.Clock()

gravity = 0.35
movement = 0

bg_img = pg.image.load('images/bg1.jpg')              

floor = pg.image.load("images/base1.png")
floor = pg.transform.scale2x(floor)
floor_x_pos = 0

not_a_trump = pg.image.load('images/UFO.png')
not_a_trump = pg.transform.scale2x(not_a_trump)
not_a_trump_rect = not_a_trump.get_rect(center = (100,325))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                movement = 0
                movement -= 10 

    window.blit(bg_img, (0,-240))
    window.blit(not_a_trump, (not_a_trump_rect))
    create_floor()
    movement += gravity
    not_a_trump_rect.centery += movement
    floor_x_pos -= 1
    if floor_x_pos <= -500:
        floor_x_pos = 0
    pg.display.update()
    watch.tick(120)