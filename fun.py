from __future__ import division
import cv2
# to show the image
from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin

green = (0, 255, 0)


def show(image):
    # Figure size in inches
    plt.figure(figsize=(10, 10))

    # Show image, with nearest neighbour interpolation
    plt.imshow(image, interpolation='nearest')


def overlay_mask(mask, image):
    # make the mask rgb
    #since the image is RGB and mask is Grayscale
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    # calculates the weightes sum of two arrays. in our case image arrays
    # input, how much to weight each.
    # optional depth value set to 0 no need
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    return img


def find_biggest_contour(image):
    # Copy
    image = image.copy()
    # input, gives all the contours, contour approximation compresses horizontal,
    # vertical, and diagonal segments and leaves only their end points. For example,
    # an up-right rectangular contour is encoded with 4 points.
    # Optional output vector, containing information about the image topology.
    # It has as many elements as the number of contours.
    # we dont need it
    _, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Isolate largest contour
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    return biggest_contour, mask


def circle_contour(image, contour):
    # Bounding ellipse
    image_with_ellipse = image.copy()
    # easy function
    ellipse = cv2.fitEllipse(contour)
    # add it
    cv2.ellipse(image_with_ellipse, ellipse, green, 2, cv2.LINE_AA)
    return image_with_ellipse


def find_strawberry(image):


    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Make a consistent size
    # get largest dimension

    max_dimension = max(image.shape)

    # The maximum window size is 700 by 660 pixels. make it fit in that
    scale = 700 / max_dimension

    # resize it. rescale width and hieght with same ratio none since output is 'image'.
    image = cv2.resize(image, None, fx=scale, fy=scale)
    image1 = image.copy()
    cv2.imwrite('image.jpg', image)
    # we want to eliminate noise from our image. clean. smooth colors without
    # dots
    # Blurs an image using a Gaussian filter. input, kernel size, how much to filter, empty)
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imwrite('image_blur.jpg', image_blur)
    # unlike RGB, HSV separates luma, or the image intensity, from
    # chroma or the color information.
    # just want to focus on color, segmentation
    image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)
    cv2.imwrite('image_blur_hsv.jpg', image_blur_hsv)
    #For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].
    # Filter by colour
    # 0-10 hue
    # minimum red amount, max red amount
    min_red = np.array([0, 100, 80])
    max_red = np.array([10, 256, 256])
    # layer
    mask1 = cv2.inRange(image_blur_hsv, min_red, max_red)
    cv2.imwrite('mask1.jpg', mask1)
    # birghtness of a color is hue
    # 170-180 hue
    min_red2 = np.array([170, 100, 80])
    max_red2 = np.array([180, 256, 256])
    mask2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)
    cv2.imwrite('mask2.jpg', mask2)

    # looking for what is in both ranges
    # Combine masks
    mask = mask1 + mask2
    cv2.imwrite('mask.jpg', mask)

    # Clean up
    # we want to circle our strawberry so we'll circle it with an ellipse
    # with a shape of 15x15
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

    # morph the image. closing operation Dilation followed by Erosion.
    # It is useful in closing small holes inside the foreground objects,
    # or small black points on the object.
    mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('mask_closed.jpg', mask_closed)
    # erosion followed by dilation. It is useful in removing noise
    mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('mask_clean.jpg', mask_clean)

    # Find biggest strawberry
    # get back list of segmented strawberries and an outline for the biggest one
    big_strawberry_contour, mask_strawberries = find_biggest_contour(mask_clean)
    cv2.imwrite('big_strawberry_contour.jpg', mask_strawberries)
    # Overlay cleaned mask on image
    # overlay mask on image, strawberry now segmented
    #this step is not necessary
    overlay = overlay_mask(mask_clean, image)
    cv2.imwrite('overlay.jpg', overlay)
    # Circle biggest strawberry
    # circle the biggest one
    circled = circle_contour(overlay, big_strawberry_contour)
    circled1 = circle_contour(image1, big_strawberry_contour)
    show(circled)
    show(circled1)

    # we're done, convert back to original color scheme
    bgr = cv2.cvtColor(circled1, cv2.COLOR_RGB2BGR)

    return bgr



# read the image
image = cv2.imread('C:/Users/Dipanker/Desktop/download1.jpg')
# detect it
result = find_strawberry(image)
# write the new image
cv2.imwrite('yo2.jpg', result)