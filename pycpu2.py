#!/usr/bin/python3

print("-------------- Welcome to PyCPU v1.0 --------------")

import psutil
import time

command = input("Choose a function:\n1. CPU Frequency (MHz)\n2. CPU Temperature (UNDER DEVELOPEMENT)\n")

if command == "1":
    unit = input("Choose unit:\n1.MHz\n2.GHz ")
    if unit == "2":
        while True:
            print(str(round(psutil.cpu_freq()[0],-1)/1000)+" GHz")
            time.sleep(0.75)