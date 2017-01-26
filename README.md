##Object Detection with OpenCV
========================================
I have used OpenCV + Python to detect strawberries in an image.
Series of operations are performed which are well documented in the code to eventually highlight the biggest strawberry in an image and then draw a green circle around it.
The code for this project is present in fun.py.

#Dependencies
=========================================
1)openCV
2)matplotlib
3)numpy

#Usage
=========================================
Run fun.py to create a new image with the detected strawberry.
The last 3 lines at the bottom of demo.py let you define the input image name and the output image name. This detection takes a split second. Deep learning would be more accurate but requires more computation currently. Sometimes you just need to quickly detect an image and don't mind handcrafted which features to look for.

#Explanation
=========================================
This code contains the following functions:

1) find_strawberry(image): this function takes image as input and returns the newly generated image with detected strawberry

##Steps
===========================================
Step-1: Convert the image Color scheme from BGR to RGB 

Step-2: Make a consistent size (perform scaling accordingly)

Step-3: Remove noise from the image.Clean,smooth Colors without dots using Gaussian Filter 

Step-4: Convert the image Color scheme from RGB to HSV
Unlike RGB,HSV seperates luma, or the image intensity, from chroma or the color information.This was done, because the main focus was on color.
For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

Step-5: Now using the property of the HSV:
Filter by colour
0-10 hue => minimum red amount, max red amount => Color of strawberry must lie in this range
and 
Filter by brightness
170-180 hue

Step-6:Now look for what is in both ranges and hence combine masks that were created in Step-5
For Best results of this Step we need to perform clean up.
	
	Step-6(a): Morph the image. Closing operation is performed which is Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

	Step-6(b): Opening operation is performed which is the sister of Closing operation for removing noise.basically it is erosion followed by dilation. It is useful in removing noise.

	**Read more about Closing and Opening operation on http://homepages.inf.ed.ac.uk/rbf/HIPR2/close.htm **

	** Eroding and Dilating : http://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html **

Step-7: Find biggest strawberry and get back list of segmented strawberries and an outline for the biggest one.

Step-8: Overlay cleaned mask on Image (I feel that this step is not necessary)

Step-9: Circle the biggest strawberry

Step-10: We're done, convert back to original color scheme

2) find_biggest_contour(image) : returns the biggest contour in the provided input.
In this function,contours were detected and a hierarchy was created
and highest contour was returned

3) Overlay_mask: take mask and image as input and returns new image in which mask is overlayed on the input image

4) circle_counter(image,contour) : returns new image with contour boundary drawn on the provided image with green color

5) show(image) : this function was to show image using matplotlib







