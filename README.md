This repository provides code files that you can use, for example, as a digital planimetry method for your research. For details, see this protocol (add it later).
These files are distributed by MIT, so you can use them to create your own software.
Next I step-by-step describe code blocks.

#Area measurement in pixels
##0. Open contours.py in your programming environment
##1. Morphological changes of the Image
  After loading analyzed image, convert it from BGR to RGB for correct display via matplotlib. And then convert it to grayscale mode to prepare for contours searching.
##2. Binarization
  The color value of each pixel in the grayscale image compare to the set threshold value. If color value exceed the threshold, pixel take a customizable maximum value, else a minimum one. In our code pixels are sorted to black (min value) and white (max value), so the output is a binary monochrome image with a clear outline of the objects.
##3. the findContours function
  cv2.RETR_TREE – contour retriever mode. It retrieves all the contours and creates a full hierarchy list start with the external one;
  cv2.CHAIN_APPROX_NONE – capproximation method enabling to sort all the contour points.
##4. Sorting
  Contoures are sorted by the sizes of their areas. Set "reverse=true" to sort descending.
##5. Contour's filtering and architecture building
  cv2.contourArea – the function computes a contour area;
  If the contour area is within setting limits, the loop starts:
  ***
    cv2.drawContours – the function draws contour outline. Sorted contours with a right size are drawn in the color analyzed image; no filtering by contour number, so the index is "-1"; set the contour color (scalar 0, 255, 0 is lime) and thickness (set the value >= 0 to draw contours out of the objects in the image).
  ***
    Size's caption:
      cv2.boundingRect – the function defines coordinates of the contour as:
        left coordinate = min x; top coordinate = min y; width = (max x – min x); height = (max y – min y).
      cv2.rectangle – the function draws a rectangle in the image. Initial coordinates (x, y), final coordinates (x+150, y-25), rectangle color is black (0, 0, 0), thickness is "-1" to fill with color completely.
      cv2.putText – the function adds a string of the text in the image. str(area) – string format conversion; (x, y) – coordinates of the bottom-left corner of the text string in the image; cv2.FONT_HERSHEY_SIMPLEX – font type; 1.0 – font scale factor; text color; thickness of the line in pixels.
#Proportion calculator

