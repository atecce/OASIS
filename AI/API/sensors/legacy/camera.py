#!/usr/bin/env python

import cv2
cam=cv2.VideoCapture(0)
ret, frame=cam.read()
cv2.imwrite("image1.jpeg",frame)
cam.release()
cv2.destroyAllWindows()

