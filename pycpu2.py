#!/usr/bin/python3

print("-------------- Welcome to PyCPU v1.0 --------------")

import psutil
import time

# Made dummy variable as an example for a string, to compare input with it.
dummy = "this is a string"

command = input("Choose a function:\n1. CPU Frequency (MHz)\n2. CPU Temperature (UNDER DEVELOPEMENT)\n")

if command == "1":
    while True:
        unit = int(input("\nChoose unit:\n1.MHz\n2.GHz\n"))
        if unit.isdigit() == True:
            unit = int(unit)
        if type(unit)==type(dummy):
            print("\nSorry, please enter a supported value\n")
        else:
            break
    while True:
        interval = input("\nChoose update interval (in seconds):\n")
        if interval.isdigit() == True:
            interval = int(interval)
        if type(interval)==type(dummy):
            print("\nSorry, please enter a supported value")
        else:
            break
    if unit == 2:
        while True:
            print(str(round(psutil.cpu_freq()[0], -1) / 1000) + " GHz")
            time.sleep(interval)
    if unit == 1:
        while True:
            print(str(round(psutil.cpu_freq()[0],2))+" MHz")
            time.sleep(interval)