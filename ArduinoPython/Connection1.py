import serial

connected = False

ser = serial.Serial('/dev/ttyACM1')

while not connected:
    serin = ser.read()
    connected = True

ser.write('1')

while ser.read() == '1':
    print (ser.read())

ser.close()
