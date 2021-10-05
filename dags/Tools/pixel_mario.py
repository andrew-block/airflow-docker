# Library to generate images - Pillow
from PIL import Image

# Library to work with arrays
import numpy as np

# Library to generate random integer values
from random import randint


class PixelMario:

    def create_pixel_mario(self):
        # Sets final image dimensions as 480x480 pixels,
        # the original 24x24 pixel image will be expanded to these dimensions
        dimensions = 480, 480

        # Hat
        ht = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Hair
        hr = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Eyes
        ey = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Mustache
        mu = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Face
        fc = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Overalls
        ov = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Buttons
        bt = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Shirt
        sh = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Hands
        ha = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Shoes
        se = (randint(0, 256), randint(0, 256), randint(0, 256))

        # Background
        bk = (randint(0, 256), randint(0, 256), randint(0, 256))

        pixel_mario = [
            [bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, ht, ht, ht, ht, ht, ht, ht, ht, bk, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, ht, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, hr, hr, hr, fc, fc, fc, fc, fc, ey, fc, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, hr, fc, hr, fc, fc, fc, fc, fc, fc, ey, fc, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, hr, fc, hr, fc, fc, fc, fc, fc, fc, ey, fc, fc, fc, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, hr, fc, hr, hr, fc, fc, fc, fc, fc, fc, mu, fc, fc, fc, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, hr, hr, fc, fc, fc, fc, fc, fc, fc, mu, mu, mu, mu, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, bk, sh, ov, ov, sh, sh, sh, ov, ov, sh, bk, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, sh, sh, sh, ov, ov, sh, sh, sh, ov, ov, sh, sh, sh, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, sh, sh, sh, ov, ov, sh, sh, sh, ov, ov, sh, sh, sh, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, sh, sh, sh, sh, sh, ov, ov, ov, ov, ov, ov, ov, sh, sh, sh, sh, sh, bk, bk, bk, bk],
            [bk, bk, bk, bk, sh, sh, sh, sh, sh, ov, bt, ov, ov, ov, bt, ov, sh, sh, sh, sh, sh, bk, bk, bk, bk],
            [bk, bk, bk, bk, ha, ha, ha, sh, ov, ov, ov, ov, ov, ov, ov, ov, ov, sh, ha, ha, ha, bk, bk, bk, bk],
            [bk, bk, bk, bk, ha, ha, ha, ha, ov, ov, ov, ov, ov, ov, ov, ov, ov, ha, ha, ha, ha, bk, bk, bk, bk],
            [bk, bk, bk, bk, ha, ha, ha, ha, ov, ov, ov, ov, ov, ov, ov, ov, ov, ha, ha, ha, ha, bk, bk, bk, bk],
            [bk, bk, bk, bk, ha, ha, ha, ov, ov, ov, ov, ov, ov, ov, ov, ov, ov, ov, ha, ha, ha, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, ov, ov, ov, ov, bk, bk, bk, ov, ov, ov, ov, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, ov, ov, ov, ov, bk, bk, bk, ov, ov, ov, ov, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, bk, se, se, se, bk, bk, bk, bk, bk, se, se, se, bk, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, bk, se, se, se, se, bk, bk, bk, bk, bk, se, se, se, se, bk, bk, bk, bk, bk, bk],
            [bk, bk, bk, bk, bk, se, se, se, se, se, bk, bk, bk, bk, bk, se, se, se, se, se, bk, bk, bk, bk, bk]
        ]

        # Convert the pixels into an array using numpy
        array = np.array(pixel_mario, dtype=np.uint8)

        # Use PIL to create an image from the new array of pixels
        array_to_image = Image.fromarray(array)
        mario = array_to_image.resize(dimensions, resample=0)
        image_location = '/home/airflow/mario/pixel_mario_#' + (str(randint(0, 999_999))) + '.png'
        mario.save(image_location)
