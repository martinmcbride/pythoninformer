# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image
from scipy import ndimage

img_in = Image.open('boat.jpg')
array = np.array(img_in)

zoom_array = ndimage.zoom(array, (0.5, 0.5, 1))

img_out = Image.fromarray(zoom_array)
img_out.save('shrink-boat.jpg')

zoom_array = ndimage.zoom(array, (2, 2, 1))

img_out = Image.fromarray(zoom_array)
img_out.save('expand-boat.jpg')

zoom_array = ndimage.zoom(array, (0.25, 1, 1))

img_out = Image.fromarray(zoom_array)
img_out.save('stretch-boat.jpg')
