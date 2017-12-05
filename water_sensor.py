#!/usr/bin/python

import serial
import time

ser1 = serial.Serial('/dev/ttyUSB0', 9600)
#ser2 = serial.Serial('/dev/ttyAMA0', 115200)

try:
        while 1:
                waktu = time.strftime ("%Y-%m-%d,%H:%M:%S,",time.gmtime())
                respon1 = ser1.readline()
                respon1 = respon1[respon1.find("#")+1:respon1.find("*")]
                #respon2 = ser2.readline()
                print waktu,respon1
                f = open('stikom.csv','a')
                #f.write(waktu, respon1, respon2)
                f.write(waktu)
                #f.write(',')
                f.write(respon1)
                f.write("\n")
                #f.write(respon2)       
except KeyboardInterrupt:
                ser.close()

