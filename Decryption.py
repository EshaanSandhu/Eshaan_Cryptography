import cv2

def Decryption_Func(image,msg_length):
    img = cv2.imread(image)
    c = {}
    d = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    
    message = ""
    for i in range(255):
        c[i] = chr(i)

    n = 0
    m = 0
    z = 0
    for i in range(msg_length):
        message = message + c[img[n, m, z]]
        n = n + 1 
        m = m + 1 
        z = (z + 1) % 3

    return message