import requests
import numpy as np
import cv2
while True:
    images = requests.get("http://(//Your Ip Address//)")
    video = np.array(bytearray(images.content),dtype = np.uint8)
    rendor = cv2.imdecode(video,-1)

    cv2.imshow('frame', rendor)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
