import psutil
# import time
#
# # Made dummy variable as an example for a string, to compare input with it.
# dummy = "This is a good example string."
#
# try:
#     test = str(round(psutil.cpu_freq()[0], -1) / 1000)
# except TypeError:
#     print("\nSorry, this device is not supported.\nPlease choose another function.\n")
#     exec(open("pycpu.py").read())
#
# while True:
#     unit = input("\nChoose unit:\n1.MHz\n2.GHz\n")
#     if unit.isdigit() == True:
#         unit = int(unit)
#     if type(unit)==type(dummy):
#         print("\nSorry, please enter a supported value\n")
#     else:
#         break
# while True:
#     interval = input("\nChoose update interval (in seconds):\n")
#     try:
#         interval = float(interval)
#     except ValueError:
#         print("You must enter a number")
#     else:
#         break
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

print(psutil.sensors_temperatures[2])