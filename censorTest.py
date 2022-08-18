import board
import digitalio
import time

trig = digitalio.DigitalInOut(board.GPIO_P29)
trig.direction = digitalio.Direction.OUTPUT

echo = digitalio.DigitalInOut(board.GPIO_P31)
echo.direction = digitalio.Direction.INPUT

def distance(TRIG,ECHO):
    trig.value = True
    time.sleep(0.001)
    trig.value = False
    
    pulseStart = time.time()
    
    while echo.value == 0:
        pulseStart = time.time()
    while echo.value == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150 
    distance = round(distance, 2)
    return distance 

trig.value = False 

try:
    while True:

        print(distance(trig,echo))
        print("cm")
        time.sleep(0.06)

except KeyboardInterrupt:
    print("stop!")
    trig.deinit()
    echo.deinit()



