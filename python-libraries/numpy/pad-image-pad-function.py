# Author:  Martin McBride
# Created: 2021-03-16
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
from PIL import Image

# Pad an image using the pad functions

img_in = Image.open('boat.jpg')
array = np.array(img_in)

padded_array = np.pad(array, ((50, 150), (80, 20), (0, 0)))

img_out = Image.fromarray(padded_array)
img_out.save('padded-boat-pad-function.jpg')

# Now set the constant value
padded_array = np.pad(array, ((50, 150), (80, 20), (0, 0)), constant_values=(128,))

img_out = Image.fromarray(padded_array)
img_out.save('padded-boat-pad-function-grey.jpg')

# Now use wrap mode
padded_array = np.pad(array, ((50, 150), (80, 20), (0, 0)), mode='wrap')

img_out = Image.fromarray(padded_array)
img_out.save('padded-boat-pad-function-wrap.jpg')
