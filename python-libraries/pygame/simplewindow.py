# Author:  Martin McBride
# Created: 2021-02-27
# Copyright (C) 2021, Martin McBride
# License: MIT

"""
Create a basic pygame window
"""

import pygame as pg

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Initialise pygame
pg.init()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Main loop, run until window closed
running = True
while running:

    # Check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


# close pygame
pg.quit()