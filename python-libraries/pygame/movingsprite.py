# Author:  Martin McBride
# Created: 2021-02-27
# Copyright (C) 2021, Martin McBride
# License: MIT

"""
A simple sprite that moves
"""

import pygame as pg
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball(pg.sprite.Sprite):

    def __init__(self, pos, velocity):
        super(Ball, self).__init__()
        self.image = pg.image.load(os.path.join('resources', 'ball.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity)


# Initialise pygame
pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create sprites
ball = Ball((100, 200), (1, 1))
group = pg.sprite.RenderPlain()
group.add(ball)

# Main loop, run until window closed
running = True
while running:

    # Check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    group.update()
    group.draw(screen)
    pg.display.flip()

    clock.tick(30)

# close pygame
pg.quit()