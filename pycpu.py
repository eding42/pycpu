#!/usr/bin/python3

print("-------------- Welcome to PyCPU v0.1 --------------")

import sensors

sensors.init()
try:
    for chip in sensors.iter_detected_chips():
        print('{} at {}' .format(chip, chip.adapter_name))
        for feature in chip:
            print('  {}: {}'.format(feature.label, feature.get_value()))
finally:
    sensors.cleanup()