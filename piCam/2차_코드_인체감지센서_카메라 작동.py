import RPi.GPIO as GPIO #gpio라이브러리
import time     #sleep사용
import picamera
import numpy as np
import cv2

cap = cv2.VedioCaptur(0)
cap.set(3,640)  #set Width
cap.set(4,480)  #set Height

#rasberrypi
GPIO.setmode(GPIO.BCM)  #gpio 모드 셋팅

pirPin = 7
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

#camera set
camera = picamera()
counter = 1

#button
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)       #Button 입력 GPIO23
#GPIO.setup(24, GPIO.OUT)

while True:
    if GPIO.input(pirPin)==GPIO.LOW:    #인체 감지되면
        time.sleep(3)   #3초 잠자기
        if GPIO.input(pirPin)==GPIO.LOW:    #인체 감지되면
            try:    
                while True: #카메라 켜고, 얼굴 인식하고, 사진 찍기
                    ret, frame = cap.read() #카메라 읽어오기
                    frame = cv2.flip(frame, -1) #Flip camera vertically
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY())
                    
                    cv2.imshow('frame', frame)  #화면에 카메라 띄우기
                    cv2.imshow('gray',gray)
                    time.sleep(1)   #1초 잠자기
                    
                    #사람 얼굴 인식
                    #사진 저장
                    #블라인드 내리기
                
            except: #두 번째 인체 감지 안되면
                 cap.release()  #카메라 종료
                 cv2.destroyAllWindows()    #모든 창 닫기
        time.sleep(3)   #3초 잠자기
    time.sleep(3)   #3초 잠자기
            
            


