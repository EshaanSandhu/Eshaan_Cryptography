import cv2
import numpy as np
def Encryption_Func(image,msg):
    img = cv2.imread(image)
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = np.uint8(d[msg[i]])
        n = n + 1 
        m = m + 1 
        z = (z + 1) % 3

    cv2.imwrite("encrypted_"+image,img)