import cv2
import numpy as np
from alarm import Alarm
from time import sleep
import pygame


class Segurança:
    def test():
        teste = [100, 50, 400, 300]

        posicao = [teste]


        video = cv2.VideoCapture(0)

        while True:
            check, img = video.read()
            imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgTh = cv2.adaptiveThreshold(
                imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10)
            imgBlur = cv2.medianBlur(imgTh, 5)
            kernel = np.ones((3, 3), np.int8)
            imgDil = cv2.dilate(imgBlur, kernel)

            for x, y, w, h in posicao:
                recorte = imgDil[y:y+h, x:x+w]
                qtPxBranco = cv2.countNonZero(recorte)
                cv2.putText(img, str(qtPxBranco), (x, y+h-10),
                            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (255, 255, 255), 1)

                if qtPxBranco > 2000:
                    
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    #Alarm.som()
                    # if test :
                    #     Alarm.som()
                    # else:
                    #     break

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

            cv2.imshow('video', img)
            cv2.waitKey(10)


Segurança.test()





# webcam = cv2.VideoCapture(0)


# if webcam.isOpened():
#     validacao, frame = webcam.read()


#     while validacao:
#         validacao, frame = webcam.read()
#         cv2.imshow('VIDEO DA WEBCAM', frame)
#         key = cv2.waitKey(5)

#         if key == 27:
#             break
