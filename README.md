#Object Detection with OpenCV

I have used OpenCV + Python to detect strawberries in an image.
Series of operations are performed which are well documented in the code to eventually highlight the biggest strawberry in an image and then draw a green circle around it.
The code for this project is present in fun.py.

#Dependencies

1)openCV

2)matplotlib

3)numpy

#Usage

Run fun.py to create a new image with the detected strawberry.
The last 3 lines at the bottom of demo.py let you define the input image name and the output image name. This detection takes a split second. Deep learning would be more accurate but requires more computation currently. Sometimes you just need to quickly detect an image and don't mind handcrafted which features to look for.

#Original Image

![download1](https://cloud.githubusercontent.com/assets/15040734/22342055/1a27902a-e419-11e6-9dc0-6f7d4215a055.jpg)

#Explanation

This code contains the following functions: 

1)find_strawberry(image): this function takes image as input and returns the newly generated image with detected strawberry

#Steps

**Step-1**: Convert the image Color scheme from BGR to RGB 

![image](https://cloud.githubusercontent.com/assets/15040734/22342062/1a519be0-e419-11e6-965c-da3e228b3b95.jpg)

**Step-2**: Make a consistent size (perform scaling accordingly)

**Step-3**: Remove noise from the image.Clean,smooth Colors without dots using Gaussian Filter

![image_blur](https://cloud.githubusercontent.com/assets/15040734/22342052/1a1f44b0-e419-11e6-95c2-8fd3b683857b.jpg)

**Step-4**: Convert the image Color scheme from RGB to HSV
            Unlike RGB,HSV seperates luma, or the image intensity, from chroma or the color information.This was done, because the main focus was on color. For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

![image_blur_hsv](https://cloud.githubusercontent.com/assets/15040734/22342053/1a1ffefa-e419-11e6-9db1-7bbf637c12fd.jpg)

**Step-5**: Now using the property of the HSV:
Filter by colour
0-10 hue => minimum red amount, max red amount => Color of strawberry must lie in this range

![mask1](https://cloud.githubusercontent.com/assets/15040734/22342061/1a50088e-e419-11e6-8932-ca13d21d2a18.jpg)

and 
Filter by brightness
170-180 hue

![mask2](https://cloud.githubusercontent.com/assets/15040734/22342063/1a58de78-e419-11e6-823e-1cf40f54db35.jpg)

**Step-6**: Now look for what is in both ranges and hence combine masks that were created in Step-5
**Combined Mask = Mask1 + Mask2**

![mask](https://cloud.githubusercontent.com/assets/15040734/22342059/1a4e8ca2-e419-11e6-8224-0f364bff259f.jpg)

For Best results of this Step we need to perform clean up.
	
Step-6(a): Morph the image. Closing operation is performed which is Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

##Closing Operation

![mask_closed](https://cloud.githubusercontent.com/assets/15040734/22342058/1a4e2316-e419-11e6-82da-f3d412e599ad.jpg)

Step-6(b): Opening operation is performed which is the sister of Closing operation for removing noise.basically it is erosion followed by dilation. It is useful in removing noise.

##Opening Operation

![mask_clean](https://cloud.githubusercontent.com/assets/15040734/22342060/1a4e8e96-e419-11e6-83e0-192167d57e14.jpg)

**Read more about Closing and Opening operation on http://homepages.inf.ed.ac.uk/rbf/HIPR2/close.htm **

**Eroding and Dilating: http://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html **

**Step-7**: Find biggest strawberry and get back list of segmented strawberries and an outline for the biggest one.

![big_strawberry_contour](https://cloud.githubusercontent.com/assets/15040734/22342056/1a2903f6-e419-11e6-8f16-fd6a7b857ba6.jpg)

**Step-8**: Overlay cleaned mask on Image (I feel that this step is not necessary)

![overlay](https://cloud.githubusercontent.com/assets/15040734/22342051/1a1f3cc2-e419-11e6-90d0-e9ee7ff3aed4.jpg)

**Step-9**: Circle the biggest strawberry

**Step-10**: We're done, convert back to original color scheme

#Final Image

![yo2](https://cloud.githubusercontent.com/assets/15040734/22342054/1a217a5a-e419-11e6-9e1a-f88af3ed92c8.jpg)

2)find_biggest_contour(image) : returns the biggest contour in the provided input.
In this function,contours were detected and a hierarchy was created
and highest contour was returned

3)Overlay_mask: take mask and image as input and returns new image in which mask is overlayed on the input image

4)circle_counter(image,contour) : returns new image with contour boundary drawn on the provided image with green color

5)show(image) : this function was to show image using matplotlib


#Credits

The credits for the original code go to gcrowder.




