import psutil

temps = psutil.sensors_temperatures()

# Made dummy variable as an example for a string, to compare input against it.
dummy = "this is a string"

print("\nTemperature Sensors Available:\n")

list(temps.keys())
for sensors in temps.keys():
    print(sensors)

while True:
    choice = input("\nChoose display method:\n1. All Devices\n2. Specific Device\n")
    if choice.isdigit() is True:
        choice = int(choice)
    if type(choice)==type(dummy):
        print("\nSorry, please enter a supported value\n")
    else:
        break
while True:
    refresh = input("\nRefresh selected data at set interval?\n1. Yes\n2. No\n")
    if refresh.isdigit() is True:
        refresh = int(refresh)
    if type(refresh)==type(dummy):
        print("\nSorry, please enter a supported value\n")
    else:
        break

if refresh == 1:
    refresh = True
    while True:
        interval = input("\nChoose an update interval [in seconds]\n")
        if interval.isdigit() is True:
            interval = int(interval)
        if type(interval) == type(dummy):
            print("\nSorry, please enter a supported value\n")
        else:
            break
else:
    refresh = False

if choice == 1:
    print()
    for name, entries in temps.items():
        print(name)
        for entry in entries:
            print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (entry.label or name, entry.current, entry.high,
                                                                        entry.critical))
        print()

if choice == 2:
    device = input("\nEnter specific device ID. Case sensitive.\n")
    device = temps[device]
    print("\nPossible Temperature Readings:\n")
    for entry in device:
        list = []
        list.append(entry.label)
        for entry in list:
            print(entry)
    core = input("\nChoose reading to display. \nEnter '1' for All Sensors \nor enter a specific sensor\n")
    print(core)
    if type(core) is not type(dummy):
        if core is 1:
            print()
            if refresh:
                while True:
                    for entry in device:
                        print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (entry.label or device, entry.current, entry.high, entry.critical))
                    time.sleep(interval)
            if not refresh:
                for entry in device:
                    print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (entry.label or device, entry.current, entry.high, entry.critical))
    else:
        print("Still working on individual parts of sensors.")
