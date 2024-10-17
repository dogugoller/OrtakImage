import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("s1.jpeg",0)
img2 = cv2.imread("s2.jpeg",0)

#Algılayıcı
orb = cv2.ORB_create()

#Tanımlayıcı
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2, = orb.detectAndCompute(img2, None)

#Eşleştirici (bruce force)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Eşleştirmeleri sırala
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

result = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(result)
plt.axis('off')
plt.savefig("Task.png", bbox_inches='tight', pad_inches=0)
plt.show()