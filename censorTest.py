import board
import digitalio
import time
from hcsr04_coral import HCSR04


leftEye = HCSR04(board.GPIO_P16,board.GPIO_P18) 
rightEye = HCSR04(board.GPIO_P29,board.GPIO_P31)


try:
    while True:
        
        print("left Eye direction : ", end = " ")
        print(leftEye.distance(),end=" ")
        print("cm")
        
        print("right Eye direction : ",end = " ")
        print(rightEye.distance(),end=" ")
        print("cm")
        time.sleep(0.06)

except KeyboardInterrupt:
    print("stop!")
    leftEye.deinit()
    rightEye.deinit()



