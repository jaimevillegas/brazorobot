#!/usr/bin/env python

################################################
# Module:   servo.py
# Created:  2 April 2008
# Author:   Brian D. Wendt
#   http://principialabs.com/
# Version:  0.3
# License:  GPLv3
#   http://www.fsf.org/licensing/
'''
Provides a serial connection abstraction layer
for use with Arduino "MultipleSerialServoControl" sketch.
'''
################################################

import serial
import time

# Assign Arduino's serial port address
#   Windows example
#     usbport = 'COM3'
#   Linux example
#     usbport = '/dev/ttyUSB0'
#   MacOSX example
#     usbport = '/dev/tty.usbserial-FTALLOK2'
#usbport = '/dev/ttyACM1'

try:
    usbport = '/dev/ttyACM0'
except:
    usbport = '/dev/ttyACM1'

# Set up serial baud rate
ser = serial.Serial(usbport, 9600, timeout=1)




def move(servo, angle):
    '''Moves the specified servo to the supplied angle.

    Arguments:
        servo
          the servo number to command, an integer from 1-4
        angle
          the desired servo angle, an integer from 0 to 180

    (e.g.) >>> servo.move(2, 90)
           ... # "move servo #2 to 90 degrees"'''

    if (0 <= angle <= 180):
        ser.write(chr(255))
        ser.write(chr(servo))
        ser.write(chr(angle))
    else:
        print("Servo angle must be an integer between 0 and 180.\n")



def init():
    move(1,90)
    move(2,90)
    move(3,90)
    move(4,90)
    move(5,90)
    move(6,90)
    
    while True:
        move(1, 0)
        time.sleep(1)
        move(1, 180)
        time.sleep(1)
    
    a = 0
    while a < 180:
        move(1, a)
        print "moving", a
        a = a + 10
        time.sleep(0.5)
    
    b = 180
    while b > 0:
        move(1, b)
        print "moving", b
        b = b - 10
        time.sleep(0.5)
    
    print "Moved"
    move(1,90)

init()