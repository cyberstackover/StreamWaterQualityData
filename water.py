import time
import serial

ser = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=1.0)

while True:
  rcv = ser.readline()
  print("\nSonar Reading: {}".format(repr(rcv)))
