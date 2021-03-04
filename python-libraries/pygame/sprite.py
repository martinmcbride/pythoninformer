# Author:  Martin McBride
# Created: 2021-02-27
# Copyright (C) 2021, Martin McBride
# License: MIT

"""
Add a simple sprite
"""

import pygame as pg
import os

class Ball(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(Ball, self).__init__()
        self.image = BALL_IMAGE
        self.surf = self.image
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)

# Initialise pygame
pg.init()

screen = pg.display.set_mode([640, 480])

# Create sprites
BALL_IMAGE = pg.image.load(os.path.join('resources', 'ball.png'))
ball = Ball(100, 200)
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
    group.draw(screen)
    pg.display.flip()

# close pygame
pg.quit()