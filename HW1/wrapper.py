import os
import cv2
from hw1 import *


def main() -> None:
    # TODO: Add in images to read
    img1 = read_image("")
    img2 = read_image("")

    # TODO: replace None with the correct code to convert img1 and img2
    img1_gray = None
    img2_gray = None

    img1_hsv = None
    img2_hsv = None

    img1_red = extract_red(img1)
    img1_green = extract_green(img1)
    img1_blue = extract_blue(img1)

    img2_red = extract_red(img2)
    img2_green = extract_green(img2)
    img2_blue = extract_blue(img2)

    img1_swap = swap_red_green_channel(img1)
    img2_swap = swap_red_green_channel(img2)

    embed_img = embed_middle(img1, img2, (60, 60))

    img1_stats = calc_stats(img1)
    img2_stats = calc_stats(img2)

    # TODO: Replace None with correct calls
    img1_shift = None
    img2_shift = None

    img1_diff = None
    img2_diff = None

    # TODO: Select appropriate sigma and call functions
    sigma = 0
    img1_noise_red = None
    img1_noise_green = None
    img1_noise_blue = None

    img2_noise_red = None
    img2_noise_green = None
    img2_noise_blue = None

    img1_spnoise = add_salt_pepper(img1_gray)
    img2_spnoise = add_salt_pepper(img2_gray)

    # TODO: Select appropriate ksize, must be odd
    ksize = 0
    img_blur = blur_image(img1_spnoise, ksize)
    img2_blur = blur_image(img2_spnoise, ksize)

    # TODO: Write out all images to appropriate files


if __name__ == '__main__':
    main()
