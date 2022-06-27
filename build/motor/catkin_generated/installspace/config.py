#!/usr/bin/env python 

from __future__ import print_function
import time
import serial

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyUSB0", 115200)
    
    # set motor operation mode to closed loop (1)
    #print("setting motor operation mode")
    #ser.write("$!MM:1\r\n")

    # set the max RPM of the motor
    #max_rpm = str(4000 / 20)
    #print("setting max rpm to " + max_rpm)
    #ser.write("$!MMRPM:" + max_rpm  +"\r\n")

    # save to memory
    #print("\nsaving params")
    #ser.write("$^MRESB\r\n")
    
    time.sleep(1)
    # run motor
    ser.write("$!MC:400\r\n")

    time.sleep(1)
    ser.close()
