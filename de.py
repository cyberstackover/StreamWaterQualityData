#!/usr/bin/python

import serial

print "Welcome to the Atlas Scientific Raspberry Pi example."

usbport = '/dev/ttyUSB0'
ser = serial.Serial(usbport,baudrate=9600,timeout=1.0)

# turn on the LEDs
ser.write("s,1\r")
#ser.write("C,1\r")

line = ""

while True:
	data = ser.read()
	if(data == "\r"):
		print "Received from sensor:" + line
		line = ""
	else:
		line = line + data
