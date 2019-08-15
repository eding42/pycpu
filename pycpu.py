#!/usr/bin/python3

print("-------------- Welcome to PyCPU v1.05 --------------")

command = input("Choose a function:\n1. CPU Frequency (MHz)\n2. CPU Temperature (UNDER DEVELOPEMENT)\n")

# Links to the cpu_freq.py script

if command == "1":
    exec(open("./source/cpu_freq.py").read())

# Links to the cpu_temp.py script

if command == "2":
    exec(open("./source/cpu_temp.py").read())
