import time, serial
from vpython import *

arduinoData = serial.Serial('com3', 115200)
time.sleep(1);
tube = cylinder(color=color.blue,radius=1,length=1,axis=vector(0,1,0))
lab = label(text='5 Volts',box=False,pos=vector(0,.2,0))

while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    dataPacket = int(dataPacket.strip('\r\n'))
    vol = (5/1023)*dataPacket
    if vol == 0:
        vol = .001

    vol = round(vol, 1)        
    tube.length = vol
    lab.text = str(vol)