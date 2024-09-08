import cv2
import matplotlib.pyplot as plt

image = cv2.imread("IMG_1587.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 95, 255, cv2.THRESH_BINARY)
#plt.imshow(binary, cmap="gray")
#plt.show()

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

good_count = []

for x in range(len(contours)):
    area = cv2.contourArea(contours[x])
    if 10000 < area < 3500000:
        image = cv2.drawContours(image, contours[x], -1, (0, 255, 0), 5)
        good_count.append(contours[x])
        x, y, w, h = cv2.boundingRect(contours[x])
        frame = cv2.rectangle(image, (x, y), (x+150, y-25,), (0, 0, 0), -1)
        cv2.putText(image, str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3)
        print(area)

plt.imshow(image)
plt.show()

print("Number of contours in image:", len(good_count))
