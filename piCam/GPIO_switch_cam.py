import RPi.GPIO as GPIO #gpio라이브러르
import time     #sleep사용
import picamera

GPIO.setmode(GPIO.BCM)  #gpio 모드 셋팅
 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)       #Button 입력 GPIO23
#GPIO.setup(24, GPIO.OUT)                                #LED 출력GPIO24
cap = picamera.VideoCapture(0)
 
try:
    while True:
         button_state = GPIO.input(23)  #버튼 상태 확인
         #인체감지 센서 쓸 땐 인체 감지 센서 출력 값>0 
         if button_state == False:      #눌러진상태면
            time.sleep(3)   #3초 동안 쉬기
            if button_state == False: #눌러진상태면
            #GPIO.output(24, True)      #출력
                print('Button Pressed...')
                while True :
                    #비디오 읽기 성공한 경우
                    ret.frame = cap.read()
                    #비디오 읽기 실패했을 경우
                    if not ret :
                        #비디오 종료
                        print("비디오 읽기 실패")
                        cap.release()
                        picamera.destroyAllWindows()      
            #3초 뒤에 버튼 안눌려 있으면
            else:
                #카메라 종료
                cap.release()
                picamera.destroyAllWindows()
                break
            
         else:
             GPIO.output(24, False)
except KeyboardInterrupt:       #ctrl-c 누를시
    GPIO.cleanup()
