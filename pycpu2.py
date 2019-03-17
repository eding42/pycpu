#!/usr/bin/python3

print("-------------- Welcome to PyCPU v1.0 --------------")

import psutil
import time

command = input("Choose a function:\n1. CPU Frequency (MHz)\n2. CPU Temperature (UNDER DEVELOPEMENT)\n")

if command == "1":
    while True:
        print(psutil.cpu_freq())
        time.sleep(1)