import cv2
import numpy as np

image = cv2.imread("makarna_resmi.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = 127

_, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


print("makarna sayısı:", len(contours))

cv2.imshow("Eşiklenmiş Görüntü", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()