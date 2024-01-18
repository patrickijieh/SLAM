import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from camera import Camera

# Orb creation

def orb_create():
  img = cv.imread("videos/img2.png", cv.IMREAD_UNCHANGED)
  orb = cv.ORB_create()
  camera = Camera()

  print(camera.get_coords())

  kp = orb.detect(img, None)

  kp, des = orb.compute(img, kp)

  img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
  plt.imshow(img2)
  plt.show()

# Main function

def main():
  print("Hello World!")
  orb_create()

if __name__ == "__main__":
  main()
