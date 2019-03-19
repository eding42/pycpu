#!/usr/bin/python3

print("-------------- Welcome to PyCPU v1.0 --------------")

import psutil
import time

command = input("Choose a function:\n1. CPU Frequency (MHz)\n2. CPU Temperature (UNDER DEVELOPEMENT)\n")

if command == "1":
    units = input("Choose unit:\n1.MHz\n2.GHz ")
    while True:
        print(round(psutil.cpu_freq()[0],-1)/1000)
        time.sleep(1)
