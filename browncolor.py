import cv2
import numpy as np

def get_limits(color):
    # Convert BGR to HSV
    if color.lower() == "blue":
        lower_limit = np.array([100, 150, 0])
        upper_limit = np.array([140, 255, 255])
    else:
        # default: detect everything
        lower_limit = np.array([0, 0, 0])
        upper_limit = np.array([179, 255, 255])
    return lower_limit, upper_limit
