import serial
arduinoData = serial.Serial('COM6', 9600)

while True:
    cmd = input("Enter a number: ")
    cmd = cmd+'\r'
    arduinoData.write(cmd.encode())