# Author:  Martin McBride
# Created: 2021-03-17
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image

img_in = Image.open('boat.jpg')
array = np.array(img_in)

flipped_array = np.flipud(array)

img_out = Image.fromarray(flipped_array)
img_out.save('flipv-boat.jpg')
