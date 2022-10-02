# Author:  Martin McBride
# Created: 2022-10-02
# Copyright (C) 2022, Martin McBride
# License: MIT

import numpy as np
from PIL import Image

array = np.zeros([100, 200, 3], dtype=np.uint8)
array[:,:100] = [255, 128, 0] #Orange left side
array[:,100:] = [0, 0, 255]   #Blue right side

img = Image.fromarray(array)
img.save('testrgb.png')


array = np.zeros([100, 200, 4], dtype=np.uint8)
array[:,:100] = [255, 128, 0, 255] #Orange left side
array[:,100:] = [0, 0, 255, 255]   #Blue right side

array[:, :, 3] = np.linspace(0, 255, 200)

img = Image.fromarray(array)
img.save('testrgba.png')


array = np.zeros([100, 200], dtype=np.uint8)

# Set grey value to black or white depending on x position
for x in range(200):
    for y in range(100):
        if (x % 16) // 8 == (y % 16) // 8:
            array[y, x] = 0
        else:
            array[y, x] = 255

img = Image.fromarray(array)
img.save('testgrey.png')