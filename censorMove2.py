import keyboard
import time 
from hcsr04_coral import HCSR04
from multiprocessing import Process, Queue

key_value_default = {'w': 0, 'a': 0, 's': 0, 'd': 0, 'q': 0, 'e': 0}
control_offset = {'IDstepLength': 0.0, 'IDstepWidth': 0.0, 'IDstepAlpha': 0.0}

class censorInterrupt():

    def __init__(self,leftCensor,rightCensor):
        
        # Set Move Speed At Certain Direction
        self.move_status = Queue()
        self.move_status.put(key_value_default)

        # Calculate Offset based on Move Status
        self.command_status = Queue()
        self.command_status.put(control_offset)

        # Offset for Robot Control
        self.X_STEP = 10.0
        self.Y_STEP = 5.0
        self.YAW_STEP = 3.0

        # left And Right RadioWave Censor
        self.leftCensor = leftCensor
        self.rightCensor = rightCensor
    
    def resetStatus(self):
        result_dict = self.move_status.get()
        self.move_status.push(key_value_default)

    def keyCounter(self,direction):
        
        result_dict = self.move_status.get()
        result_dict[direction] +=1
        self.move_status.put(result_dict)
    
    def setSpeed(self,direction,speed):
        result_dict = self.move_status.get()
        if (speed < 15):
            result_dict[direction] = speed
            self.move_status.put(result_dict)

    def stopMoveToDirection(self,direction):

        result_dict = self.move_status.get()
        result_dict[direction] = 0
        self.move_status.put(result_dict)
    
    def goStraight():
        
        result_dict = key_value_default
        result_dict['w'] = 3
        self.move_status.put(result_dict)
    
    def goBack():

        result_dict = key_value_default
        result_dict['s'] = 3
        self.move_status.put(result_dict)

    def stop():
        
        result_dict= key_value_default
        self.move_status.put(result_dict)

    def leftRotate():

        result_dict = key_value_default
        result_dict['q'] = 3
        self.move_status.put(result_dict)
    
    def rightRotate():
    
        result_dict = key_value_default
        result_dict['e'] = 3
        self.move_status.put(result_dict)
   

    def calcRbStep(self):
        result_dict = self.move_status.get()
        command_dict = self.command_status.get()
        command_dict['IDstepLength'] = self.X_STEP * result_dict['s'] - self.X_STEP * result_dict['w']
        command_dict['IDstepWidth'] = self.Y_STEP * result_dict['d'] - self.Y_STEP * result_dict['a']
        command_dict['IDstepAlpha'] = self.YAW_STEP * result_dict['q'] - self.YAW_STEP * result_dict['e']

        self.move_status.put(result_dict)
        self.command_status.put(command_dict)



    # Move Direction is Decided By Distance

    def censorInterrupt(self,id, move_status, command_status):

        was_pressed = False

        while True:

            leftDirection = self.leftCensor.distance()
            rightDirection = self.rightCensor.distance()
            
            if (leftDirection < 10 && rightDirection < 10):
                leftRotate()
            else:
                goStragiht()
 
            time.sleep(0.06)
            calcRbStep()
        
           


