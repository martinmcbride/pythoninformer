# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image

img_in = Image.open('boat.jpg')
array = np.array(img_in)

cropped_img = array[50:350, 150:450, :]

img_out = Image.fromarray(cropped_img)
img_out.save('cropped-boat.jpg')
