                                ##########################
                                #                        #
                                # Autor Villani Fabrizio #
                                #                        #
                                ##########################

# import Adafruit_PCA9685
#
# import time
# #import RPi.GPIO as GPIO



#initialisation
# pin1 = 11
# pin2 = 12
# pin3 = 13
pin4 = 15

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(pin1,GPIO.OUT)#Back
# GPIO.setup(pin2,GPIO.OUT)#Front
# GPIO.setup(pin3,GPIO.OUT)#Back
# GPIO.setup(pin4,GPIO.OUT)#Front
#
# servo = Adafruit_PCA9685.PCA9685()
# servo.set_pwm_freq(50)

import threading
import time



class ServoMotor(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.s = s

    def run(self):
        # condition = True
        # while condition:
            #motor.set_pwm(Lepin,0,100)
            #motor.set_pwm(Lepin,0,100)
        for i in range(0,10):
            print("thread  " , self.s , " : ", i, "\n")
            time.sleep(0.09)  # attend 100 millisecondes sans rien faire
            # condition = False


m = ServoMotor( "A")
m.start()

m2 = ServoMotor( "B")  # contien le thread des ultrasons
m2.start()




# while condition2:
#     condition2=True
for i in range(0,10):
    print("Programme  " ,i )
    time.sleep(0.1)
    # condition2 = False






# class Motor(Servo):
#     def __init__(self):
#         super().__init__()
#         print("Init Motor")
#
#     def moveDirection(self,vitesse,pin1,pin2):
#
#
#
#
#     def forward(self,vitesse):
#         i = int(input("entre une vitesse"))
#         #Je mets la vitesse au moteur !!
#         print("avance d'une vitesse de ", i)
#
#     def stopForward(self):
#         print("stop avance")
#
#     def retrat(self,vitesse):
#         i = int(input("entre une vitesse"))
#         print("recule d'une vitesse de ", i)
#
#     def stopRetrat(self):
#         print("stop recule")
#
#     def demitour(selfs, degre):
#         i = int(input("entre un degres"))
#         # servo.set_pwm(0,0,i)
#
#










