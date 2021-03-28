# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image
from scipy import ndimage
import math

img_in = Image.open('boat.jpg')
array = np.array(img_in)

def transform(output_coords):
    return output_coords[0]%200, output_coords[1]%300, output_coords[2]

transformed_array = ndimage.geometric_transform(array, transform)

img_out = Image.fromarray(transformed_array)
img_out.save('geo-boat.jpg')
