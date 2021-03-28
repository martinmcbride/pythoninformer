# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image
from scipy import ndimage

img_in = Image.open('boat.jpg')
array = np.array(img_in)

height, width, colors = array.shape

transform = [[1, 0, 0],
             [0.5, 1, 0],
             [0, 0, 1]]
sheared_array = ndimage.affine_transform(array,
                                         transform,
                                         offset=(0, -height//2, 0),
                                         output_shape=(height, width+height//2, colors))

img_out = Image.fromarray(sheared_array)
img_out.save('shear-boat.jpg')
