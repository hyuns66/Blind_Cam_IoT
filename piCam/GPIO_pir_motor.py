import RPi.GPIO as GPIO
import time
import sys
from collections import deque

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pir 센서 핀
pir_signal = 17
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
    print("main")
    motor_rotate()

def motor_rotate():

    try:
        while 1:
            for cnt in range(0, step):
                GPIO.output(motor_in1, sig[0])
                GPIO.output(motor_in2, sig[1])
                GPIO.output(motor_in3, sig[2])
                GPIO.output(motor_in4, sig[3])
                time.sleep(0.001)
                sig.rotate(dir)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()