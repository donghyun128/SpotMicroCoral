import board
import digitalio
import time

class HCSR04:

    def __init__(self, trig_pin, echo_pin):

        self.trig = digitalio.DigitalInOut(trig_pin)
        self.trig.direction = digitalio.Direction.OUTPUT

        self.echo = digitalio.DigitalInOut(echo_pin)
        self.echo.direction = digitalio.Direction.INPUT
        
        self.trig.value = False

    """
    distance: return centimeter distance measured by hcsr04 Ultrasonic censor
    """
    def distance(self):
        self.trig.value = True
        time.sleep(0.00001)
        self.trig.value = False
        
        pulseStart = time.time()

        while self.echo.value == 0:
            pulseStart = time.monotonic()
        while self.echo.value == 1:
            pulseEnd = time.monotonic()

        pulseDuration = pulseEnd - pulseStart
        # distance [cm] = speed of ultrasonic wave * round trip time = 340 [m/s] * pulseDuration [s] / 2 * 100 [cm/m]
        distance = pulseDuration * 34000 
        distance = round(distance, 2)
        return distance 
     
    
    def deinit(self):
        self.trig.deinit()
        self.echo.deinit()




