import serial
import threading
import time

ser = {}
# Spin 30, 2, 2000
# linear 12, 0, 1500
# 25, 8, 2000
PID = [20, 0, 1000]
#PID = [12, 0, 3000]
#PID = [30, 2, 4000]
#PID = [40, 2, 1000]
#PID = [12, 0, 1500]
max_rpm = 4000 
max_acc = 1000
mode = 1 
_set = True
#_set = False 
def printSerRead(ser):
    print(ser.readline())

def getSerial(id):
    return serial.Serial('/dev/ttyMOTOR' + str(id), 115200, timeout=0.5, write_timeout=0.5)

def closeSerial(ser):
    ser.close()

def printPID(ser):
    PID = ['MKP', 'MKI', 'MKD']

    ser.write(b'$?MKP\r\n')
    line = ser.readline()
    print(line)
    while line[2:5] != 'MKP':
        line = ser.readline()
        print(line)
    
    ser.write(b'$?MKI\r\n')
    line = ser.readline()
    print(line)
    while line[2:5] != 'MKI':
        ser.write(b'$?MKI\r\n')
        line = ser.readline()
        print(line)

    ser.write(b'$?MKD\r\n')
    line = ser.readline()
    print(line)
    while line[2:5] != 'MKD':
        ser.write(b'$?MKD\r\n')
        line = ser.readline()
        print(line)

def printAllConfigure(ser):
    PIDName = ['MPP', 'MKP', 'MKI', 'MKD', 'MMR', 'MAC', 'MDE', 'MBK', 'MAMP']
    try:
        for i in range(14):
            ser.write(b'$??\r\n')

            line = ser.readline()
            if line[1] == '?':
                if line[2:5] in PIDName:
                    print("PID Value")
                    print(i, line)
                elif line[2:4] == 'MM':
                    print("Motor Mode")
                    print(i, line)
                elif line[2:6] == 'MAMP':
                    print("Current Limit")
                    print(i, line)
    except:
        print("no data")

def setPID(ser, PID):
    for i in range(14):
        ser.write(b'$!MKP:{}\r\n'.format(PID[0]))
        ser.write(b'$!MKI:{}\r\n'.format(PID[1]))
        ser.write(b'$!MKD:{}\r\n'.format(PID[2]))
    #printAllConfigure(ser)
def setMaxRPM(ser, _max_rpm):
    for i in range(14):
        ser.write(b'$!MMRPM:{}\r\n'.format(_max_rpm))
def setMaxACC(ser, _max_acc):
    for i in range(14):
        ser.write(b'$!MAC:{}\r\n'.format(_max_acc))
        ser.write(b'$!MDEC:{}\r\n'.format(_max_acc))
def setMode(ser, _mode):
    for i in range(14):
        ser.write(b'$!MM:{}\r\n'.format(_mode))

def setStopBrakingTimeout(ser, _time=4000):
    for i in range(14):
        ser.write(b'$!MBK:{}\r\n'.format(_time))

def saveConfiguration(ser):
    for i in range(14):
        ser.write(b'$^MSAV\r\n')

sers = []
# 40, 2, 1000
for i in range(2):
    sers.append(getSerial(i + 2))
    #printAllConfigure(sers[i])
#    print(sers[i].name)
    if _set:
        setPID(sers[i], PID)
        setMaxRPM(sers[i], max_rpm)
        setMaxACC(sers[i], max_acc)
        setMode(sers[i], mode)
        setStopBrakingTimeout(sers[i], 2000)
        saveConfiguration(sers[i])
    time.sleep(0.500)
    print("Configurations for " + str(i))
    printAllConfigure(sers[i])
    time.sleep(0.500)
    closeSerial(sers[i])

#for i in range(4):
#    sers[i].close()

