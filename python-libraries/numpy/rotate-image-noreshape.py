# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image
from scipy import ndimage

img_in = Image.open('boat.jpg')
array = np.array(img_in)

rotated_array = ndimage.rotate(array, 45, reshape=False, cval=128)

img_out = Image.fromarray(rotated_array)
img_out.save('rotate-boat-noreshape.jpg')
