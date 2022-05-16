# import RPi.GPIO as GPIO
# from time import sleep
#
# def main():
#     led = 22
#     switch = 23
#     state = 1
#
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(led, GPIO.OUT)
#     GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)
#
#     try:
#         while True:
#             if GPIO.input(switch) == 0:
#                 while True:
#                     if GPIO.input(switch) == 1:
#                         state = not state
#                         GPIO.output(led, state)
#                         sleep(0.2)
#                         break
#
#     finally:
#         print("end")
#
# if __name__ == "__main__":
#     main()



import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
echo = 22
trigger = 23
print("start")

GPIO.setwarnings(False)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

while True:
    try:
        GPIO.output(trigger, False)
        time.sleep(0.5)
        GPIO.output(trigger, True)
        time.sleep(0.00001)
        GPIO.output(trigger, False)

    while GPIO.input(echo) == 0:
        StartTime = time.time()
        print("asdf")

    while GPIO.input(echo) == 1:
        StartTime = time.time()
        print("fdas")

    TimeElapsed = StopTime - StartTime
    distnace = round((TimeElapsed * 34300) / 2, 2)
    print("Distance = ", distance, "cm")
    time.sleep(1)

except KeyboardInterrupt:
    sys.exit(0)