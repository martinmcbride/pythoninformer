# Author:  Martin McBride
# Created: 2021-02-27
# Copyright (C) 2021, Martin McBride
# License: MIT

"""
A simple sprite that bounces
"""

import pygame as pg
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball(pg.sprite.Sprite):

    def __init__(self, pos):
        super(Ball, self).__init__()
        self.image = pg.image.load(os.path.join('resources', 'ball.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = [5, 5]

    def update(self):
        if self.rect.left < 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity[1] *= -1
        self.rect.move_ip(self.velocity)


# Initialise pygame
pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create sprites
ball = Ball((100, 200))
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