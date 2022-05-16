import RPi.GPIO as GPIO
from time import sleep

def main():
    led = 22
    switch = 23
    state = 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)

    try:
        while True:
            if GPIO.input(switch) == 0:
                while True:
                    if GPIO.input(switch) == 1:
                        state = not state
                        GPIO.output(led, state)
                        sleep(0.2)
                        break

    finally:
        print("end")

if __name__ == "__main__":
    main()



# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
# switch = 23
# led = 24
# print("start")
#
# GPIO.setup(led, GPIO.OUT)
# GPIO.setup(switch, GPIO.IN)
#
# try:
#     while True:
#     StartTime = time.time()
#     StopTime = time.time()
#     GPIO.output(led, True)
#     time.sleep(0.00001)
#     GPIO.output(led, False)
#
#     while GPIO.input(switch) == 0:
#         StartTime = time.time()
#
#     while GPIO.input(switch) == 1:
#         StartTime = time.time()
#
#     TimeElapsed = StopTime - StartTime
#     distnace = round((TimeElapsed * 34300) / 2, 2)
#     print("Distance = ", distance, "cm")
#     time.sleep(1)
#
# except KeyboardInterrupt:
#     pass