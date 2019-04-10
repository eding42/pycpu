import psutil
import time

# Made dummy variable as an example for a string, to compare input with it.
dummy = "this is a string"

while True:
    unit = input("\nChoose unit:\n1.MHz\n2.GHz\n")
    if unit.isdigit() == True:
        unit = int(unit)
    if type(unit)==type(dummy):
        print("\nSorry, please enter a supported value\n")
    else:
        break
while True:
    interval = input("\nChoose update interval (in seconds):\n")
    try:
        interval = float(interval)
    except ValueError:sssss
        print("You must enter a number")
    else:
        break
if unit == 2:
    while True:
        print(str(round(psutil.cpu_freq()[0], -1) / 1000) + " GHz")
        time.sleep(interval)
if unit == 1:
    while True:
        print((round(psutil.cpu_freq()[0],2))+" MHz")
        time.sleep(interval)