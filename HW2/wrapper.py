import os
import cv2
from hw2 import *


"""
This assignment will have you detect various traffic signs and traffic lights.
When trying to find a sign, it's helpful to mask the sign based on color range in HSV.
OpenCV uses the following ranges for HSV, H: 0-179, S: 0-255, V: 0-255
Photoshop uses the followwing ranges: H: 0-360, S: 0-100, V: 0-100

So when grabbing the values from other programs, keep in mind how they represent the values and adjust accordingly

If you're looking at the pixel values from the numpy array, remember that the x and y are reversed when you slice it

A typical process would be to convert the image to HSV, identify the pixels that contain the sign in question,
create a low and high bounds for the color in HSV, then use the inRange on the HSV image to get the mask.
Then do the normal edge detection, HoughLinesP/HoughCircles.
"""


def main() -> None:
    part1()
    part2()
    part3()
    part4()
    part5()


def part1() -> None:
    """
    Part 1 is identifying a traffic light along with which one is lit
    :return: None
    """
    tl_images = ['images/tl_all_bright_default.jpg',
                 'images/tl_red_bright_default.jpg', 'images/tl_green_bright_default.jpg',
                 'images/tl_yellow_bright_default.jpg', 'images/background_img_tl_red_bright.jpg',
                 'images/background_img_tl_red_bright2.jpg', 'images/background_img_tl_green_bright.jpg',
                 'images/background_img_tl_yellow_bright.jpg']

    for tl in tl_images:
        tl_image = cv2.imread(tl)
        x, y, color = identify_traffic_light(tl_image)
        img_out = mark_signs(tl_image, (x, y), color)
        cv2.imwrite(f"{tl.split('/')[1].split('.')[0]}_txt.jpg", img_out)


def part2() -> None:
    sign_images = ['images/construction.jpg', 'images/regulatory.jpg', 'images/regulatory_yield.jpg',
                   'images/rr_crossing.jpg', 'images/services.jpg', 'images/warning.jpg']

    file_name = ['construction_txt.jpg', 'regulatory_txt.jpg', 'regulatory_yield_txt.jpg',
                 'rr_crossing_txt.jpg', 'services_txt.jpg', 'warning_txt.jpg']

    sign_functions = [identify_construction, identify_stop_sign, identify_yield,
                      identify_rr_crossing, identify_services, identify_warning]

    for img_in, file_out, function_call in zip(sign_images, file_name, sign_functions):
        img = cv2.imread(img_in)
        x, y, name = function_call(img)

        img_out = mark_signs(img, (x, y), state=name)
        cv2.imwrite(file_out, img_out)


def part3() -> None:
    sign_images = ['images/all_signs_blank_background.jpg', 'images/all_signs.jpg',
                   'images/construction_warning_rr_crossing_background.jpg', 'images/construction_warning_rr_crossing_background02.jpg',
                   'images/stop_sign_background.jpg', 'images/stop_sign_background02.jpg', 'images/stop_yield_background.jpg',
                   'images/stop_yield_background02.jpg']

    file_name = ['all_signs_blank_background_txt.jpg', 'all_signs_txt.jpg',
                 'construction_warning_rr_crossing_background_txt.jpg', 'construction_warning_rr_crossing_background02_txt.jpg',
                 'stop_sign_background_txt.jpg', 'stop_sign_background02_txt.jpg', 'stop_yield_background_txt.jpg',
                 'stop_yield_background02_txt.jpg']

    for img_in, file_out in zip(sign_images, file_name):
        img = cv2.imread(img_in)
        img_out = np.copy(img)
        found_signs = identify_signs(img)
        # print(found_signs)
        if found_signs:
            for sign in found_signs:
                x = sign[0]
                y = sign[1]
                name = sign[2]
                img_out = mark_signs(img_out, (x, y), name)
            # print("writing file")
            cv2.imwrite(file_out, img_out)


def part4() -> None:
    # print("in part 4")
    sign_images = ['images/all_signs_blank_background_noise.jpg', 'images/all_signs_noise.jpg']

    file_name = ['all_signs_blank_background_noise_txt.jpg', 'all_signs_noise_txt.jpg']

    for img_in, file_out in zip(sign_images, file_name):
        img = cv2.imread(img_in)
        img_out = np.copy(img)
        found_signs = identify_signs_noisy(img)
        if found_signs:
            for sign in found_signs:
                x = sign[0]
                y = sign[1]
                name = sign[2]
                img_out = mark_signs(img_out, (x, y), name)

            cv2.imwrite(file_out, img_out)


def part5() -> None:
    sign_images = ['images/real_signs01.jpg', 'images/real_signs02.jpg', 'images/real_signs03.jpg']

    file_name = ['real_signs01_txt.jpg', 'real_signs02_txt.jpg', 'real_signs03_txt.jpg']

    for img_in, file_out in zip(sign_images, file_name):
        img = cv2.imread(img_in)
        img_out = np.copy(img)
        found_signs = identify_signs_real(img)
        if found_signs:
            for sign in found_signs:
                x = sign[0]
                y = sign[1]
                name = sign[2]
                img_out = mark_signs(img_out, (x, y), name)

            cv2.imwrite(file_out, img_out)


def mark_signs(image, coords, state='') -> np.ndarray:
    img = cv2.putText(image, f"x: {coords[0]}, y: {coords[1]}", (coords[0]+5, coords[1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0), 3)
    img = cv2.putText(img, f"x: {coords[0]}, y: {coords[1]}", (coords[0]+5, coords[1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1)
    cv2.circle(img, (coords[0], coords[1]), 2, (0, 0, 0), -1)
    if state != '':
        img = cv2.putText(img, f"{state}", (coords[0]+5, coords[1]+15), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0), 3)
        img = cv2.putText(img, f"{state}", (coords[0]+5, coords[1]+15), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1)
    return img


if __name__ == '__main__':
    main()
