import psutil

temps = psutil.sensors_temperatures()

# Made dummy variable as an example for a string, to compare input against it.
dummy = "this is a string"


# # Made dummy variable as an example for a string, to compare input with it.
# dummy = "This is a good example string."
#
# if unit == 1:
#     while True:
#         print(str(round(psutil.sensors_temperatures[0],2))+" MHz")
#         time.sleep(interval)
#
# if unit == 2:
#     while True:
#         print(str(round(psutil.cpu_freq()[0], -1) / 1000) + " GHz")
#         time.sleep(interval)

# try:
#     test = str(round(psutil.sensors_temperatures()[0], -1))
# except TypeError:
#     print("\nSorry, this device is not supported.\nPlease choose another function.\n")
#     exec(open("../pycpu.py").read())

while True:
    choice = input("\nChoose display method:\n1. All Devices\n2. Specified Device\n")
    if choice.isdigit() == True:
        choice = int(choice)
    if type(choice)==type(dummy):
        print("\nSorry, please enter a supported value\n")
    else:
        break
while True:
    refresh = input("\nRefresh selected data at set interval?\n1. Yes\n2. No\n")
    if refresh.isdigit() == True:
        refresh = int(refresh)
    if type(refresh)==type(dummy):
        print("\nSorry, please enter a supported value\n")
    else:
        break
if choice == 1:
    for name, entries in temps.items():
        print(name)
        for entry in entries:
            print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (entry.label or name, entry.current, entry.high,entry.critical))
        print()