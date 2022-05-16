import RPi.GPIO as GPIO #gpio라이브러리
import time     #sleep사용
import picamera
import numpy as np
import cv2
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from uuid import uuid4
from collections import deque
import sys

cap = cv2.VedioCaptur(0)
cap.set(3,640)  #set Width
cap.set(4,480)  #set Height

#firebase && capture
PROJECT_ID = "iot-rpi-blind"

cred = credentials.Certificate("./serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': f"{PROJECT_ID}.appspot.com"    
})
bucket = storage.bucket()

def fileUpload(file):
    blob = bucket.blob('Images/'+file)
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}
    blob.metadata = metadata

    blob.upload_from_filename(filename='./Images/'+file, content_type='image/jpeg')
    print(blob.public_url)

def execute_camera():
    subtitle = "Ras"
    suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
    filename = "_".join([subtitle, suffix])

    camera = PiCamera()
    camera.capture('/home/pi/Images/' + filename)
    fileUpload(filename)
    
#motor_rotate code    
def motor_rotate():

    try:
        max_time_end = time.time() + (5) #초단위
        while True:
            for cnt in range(0, step):
                GPIO.output(motor_in1, sig[0])
                GPIO.output(motor_in2, sig[1])
                GPIO.output(motor_in3, sig[2])
                GPIO.output(motor_in4, sig[3])
                time.sleep(0.002)
                sig.rotate(dir)
            if time.time() > max_time_end:
                break

    except KeyboardInterrupt:
        sys.exit(0)

#motor_rotate code 리버스  
def motor_rotate_r():

    try:
        max_time_end = time.time() + (5)
        while True:
            for cnt in range(0, step):
                GPIO.output(motor_in1, sig[3])
                GPIO.output(motor_in2, sig[2])
                GPIO.output(motor_in3, sig[1])
                GPIO.output(motor_in4, sig[0])
                time.sleep(0.002)
                sig.rotate(dir)
            if time.time() > max_time_end:
                break

    except KeyboardInterrupt:
        sys.exit(0)

        
#rasberrypi
GPIO.setmode(GPIO.BCM)  #gpio 모드 셋팅
GPIO.setwarnings(False)

pirPin = 7
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

#camera set
camera = picamera()
counter = 1

# 모터 핀
motor_in1 = 19
motor_in2 = 26
motor_in3 = 20
motor_in4 = 21

GPIO.setup(motor_in1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motor_in2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motor_in3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motor_in4, GPIO.OUT, initial=GPIO.LOW)

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
                    
                    #사람 얼굴 인식 #사진 저장
                    faces = face_cascade.detectMultiScale(gray.scaleFactor=1.4, minNeighbors=5, minSize=(40,40),maxSize(400,400))

                    if len(faces):
                        if GPIO.input(pirPin)==GPIO.HIGH:
                        execute_camera() #캡쳐 후 Image파일에 업로드
                    
                        #블라인드 내리기
                        motor_rotate()
                        sleep(5)
                        motor_rotate_r()
                        #5초 기다린 후 블라인드 올리기(motor_rotate반대로 돌리는 함수로 하면 될 긋)
                            
                
            except: #두 번째 인체 감지 안되면
                 cap.release()  #카메라 종료
                 cv2.destroyAllWindows()    #모든 창 닫기
        time.sleep(3)   #3초 잠자기
    time.sleep(3)   #3초 잠자기
            
            


