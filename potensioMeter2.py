import time, serial
import numpy as np
from vpython import *


arrowLength = 1
arrowWidth = .02
myArrow = arrow(length=arrowLength, shaftwidth=arrowWidth, color=color.red)

boxX = 2.5
boxY = 1.5
boxZ = .1
myCase = box(color=color.white,size=vector(boxX,boxY,boxZ),pos=vector(0,.9*boxY/2,-boxZ))

tickL = .1
tickW = .05
tickH = .05

for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    tickMajor = box(color=color.black,pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL,tickW,tickH),axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))


arduinoData = serial.Serial('com3', 115200)
time.sleep(1)

while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = int(dataPacket.strip('\r\n'))
    potVal = dataPacket

    theta = -2*np.pi/3069*potVal+5*np.pi/6
    myArrow.axis = vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)

    # for theta in np.linspace(np.pi/6,(5*np.pi)/6,150):
    #     rate(25)
    #     myArrow.axis = vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)

    # for theta in np.linspace((5*np.pi)/6,np.pi/6,150):
    #     rate(25)
    #     myArrow.axis = vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
    

            




    
