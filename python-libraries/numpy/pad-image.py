# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image

img_in = Image.open('boat.jpg')
array = np.array(img_in)

padded_img = np.empty([600, 700, 3], dtype=np.uint8)
padded_img[:,:] = np.array([0, 64, 128])
padded_img[50:450, 80:680] = img_in

img_out = Image.fromarray(padded_img)
img_out.save('padded-boat.jpg')
