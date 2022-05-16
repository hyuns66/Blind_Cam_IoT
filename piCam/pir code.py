import RPi.GPIO as GPIO #gpio라이브러리
import time     #sleep사용
import numpy as np

#rasberrypi
GPIO.setmode(GPIO.BCM)  #gpio 모드 셋팅

#pir 설정
pirPin = 17
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

while True:
    if GPIO.input(pirPin)==GPIO.LOW:    #인체 감지되면
        time.sleep(3)   #3초 잠자기
        if GPIO.input(pirPin)==GPIO.LOW:    #인체 감지되면
            try:    
                while True: #카메라 켜고, 얼굴 인식하고, 사진 찍기
                    print("사람이 인식되었어요")
                    time.sleep(1)   #1초 잠자기
                
            except: #두 번째 인체 감지 안되면
                 print("사람이 업서용~")
        time.sleep(3)   #3초 잠자기
    time.sleep(3)   #3초 잠자기
            
            


