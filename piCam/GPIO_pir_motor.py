import RPi.GPIO as GPIO
import time
import sys
from collections import deque
from picamera import PiCamera
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from uuid import uuid4
import numpy as np
import cv2


# 파이어베이스 프로젝트 연동
PROJECT_ID = "iot-rpi-blind"

cred = credentials.Certificate("./serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': f"{PROJECT_ID}.appspot.com"
})
bucket = storage.bucket()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 스위치 input 핀
switch = 17
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 모터 핀
motor_in1 = 19
motor_in2 = 26
motor_in3 = 20
motor_in4 = 21

GPIO.setup(motor_in1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motor_in2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motor_in3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(motor_in4, GPIO.OUT, initial=GPIO.LOW)

sig = deque([1,0,0,0])
step = 1200
dir = 1

print("start")

GPIO.setwarnings(False)

def main():
    # motor_rotate()
    set_switch_interrupt()
    while True:
        time.sleep(1)

def motor_rotate(dir):

    try:
        for cnt in range(0, step):
            GPIO.output(motor_in1, sig[0])
            GPIO.output(motor_in2, sig[1])
            GPIO.output(motor_in3, sig[2])
            GPIO.output(motor_in4, sig[3])
            time.sleep(0.002)
            sig.rotate(dir)

    except KeyboardInterrupt:
        sys.exit(0)

def pir_detect():
    while True:
        if GPIO.input(pir_signal) == GPIO.LOW:  # 인체 감지되면
            time.sleep(3)  # 3초 잠자기
            print("oh shit!!")
            if GPIO.input(pir_signal) == GPIO.LOW:  # 인체 감지되면
                print("heyy~~~~~~~~")
                time.sleep(1)  # 1초 잠자기
            else:  # 두 번째 인체 감지 안되면
                print("bye~~~~~~~~")
        else:
            time.sleep(1)
            print("nooo,,,,,,,,,,,,,")

def button_pressed_callback(channel):

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # WIDTH
    cap.set(4, 480)  # HEIGHT
    startTime = time.time()
    curtime = time.time()

    # 얼굴 인식 캐스케이드 파일 읽는다
    face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')

    while (curtime-startTime < 10):
        # frame 별로 capture 한다
        ret, frame = cap.read()
        time.sleep(0.001)
        curtime = time.time()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20))

        # 인식된 얼굴 갯수를 출력
        print(len(faces))

        if len(faces) > 0:
            motor_rotate(1)
            subtitle = "Ras"
            suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
            filename = "_".join([subtitle, suffix])

            cv2.imwrite('pictures/' + filename, frame)
            fileUpload(filename)
            isGone(cap)
            break

    cap.release()
    cv2.destroyAllWindows()
    print("end!!")

def isGone(cap):
    cap.set(3, 640)  # WIDTH
    cap.set(4, 480)  # HEIGHT
    startTime = time.time()
    curtime = time.time()

    # 얼굴 인식 캐스케이드 파일 읽는다
    face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')

    while (curtime - startTime < 5):
        # frame 별로 capture 한다
        ret, frame = cap.read()
        time.sleep(0.001)
        curtime = time.time()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20))

        if len(faces) > 0:
            startTime = time.time

    motor_rotate(-1)

def set_switch_interrupt():
    GPIO.add_event_detect(switch, GPIO.FALLING,
                          callback=button_pressed_callback, bouncetime=100)

# 파이어베이스에 사진 업로드
def fileUpload(file):
    blob = bucket.blob('man/'+file)
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}
    blob.metadata = metadata

    blob.upload_from_filename(filename='pictures/'+file, content_type='image/jpeg')
    print(blob.public_url)

def execute_camera():
    subtitle = "Ras"
    suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
    filename = "_".join([subtitle, suffix])

    camera = PiCamera()
    camera.capture('pictures/' + filename)
    fileUpload(filename)
    camera.close()

if __name__ == "__main__":
    main()