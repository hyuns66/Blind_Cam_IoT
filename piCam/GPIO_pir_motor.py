import RPi.GPIO as GPIO
import time
import sys
from collections import deque

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
step = 400
dir = 1

print("start")

GPIO.setwarnings(False)

def main():
    # motor_rotate()
    switch_read()
    while True:
        time.sleep(1)

def motor_rotate():

    try:
        while 1:
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
    print("Button pressed!")

def switch_read():
    GPIO.add_event_detect(switch, GPIO.FALLING,
                          callback=button_pressed_callback, bouncetime=100)

if __name__ == "__main__":
    main()