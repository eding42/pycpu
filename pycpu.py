#!/usr/bin/python3

print("-------------- Welcome to PyCPU v1.0 --------------")

command = input("Choose a function:\n1. CPU Frequency (MHz)\n2. CPU Temperature (UNDER DEVELOPEMENT)\n")

# Links to the cpu_freq.py script

if command == "1":
    exec(open("cpu_freq.py").read())

if command == "2":
    exec(open("cpu_temp.py").read())