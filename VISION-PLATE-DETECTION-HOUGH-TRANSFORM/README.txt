Functions

***hough_lines_transform -> Realizes the Hough Line Transform and draws lines on the original image.
***main -> It reads the photo, applies Canny edge detection and sends it to the hough_lines_transform function. 
It also shows edge image and image with detected line.

***I plotted using edge_pixels on photos where I could find corner points with a method I noticed while implementing.

***For Cars3 and Cars8, I plotted the plate with the cv2.line functions without for loop.


***For other photos whose plate I could detect, I used the part with for loop. 
In these photos I also changed the accumulator range in edge_pixels2 = np.where (accumulator> 150).


-----Threshold and Accumulator Values-----

Cars3 -> 605 1250
Cars4 -> 640 1245 - Accumulator> 300
Cars8 -> 300 1110
Cars34 -> 319 969 - Accumulator> 100
Cars37 -> 250 925 - Accumulator> 90
Cars73 -> 490 865 - Accumulator> 150
Cars74 -> 360 900 - Accumulator> 200

Cars0 - 300 500 (Undetectable)
Cars1 - 300 690 (Undetectable)
Cars2 - 200 350 (Undetectable)
Cars5 - 250 600 (Undetectable)
Cars7 - 300 500 (Undetectable)