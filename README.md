# PyCPU - A simple CPU monitoring tool

This is an implementation of the psutil module, by Giampaolo Rodola, and was created for learning purposes.

The script uses the psutil module to collect data about your CPU and system, then outputs it in the console. 

# Functionality and Features
### Current Features

1. CPU Frequency (MHz)

### Planned Features

2. CPU Temperature - Work in progress

3. CPU Utilization (%) - Planned

4. CPU Core Count - Planned

5. CPU Advanced Stats (CTX Switches, Interrupts, etc) - Planned

# Supported Systems (So Far)
**Please note that this list is far from complete. Just because your system isn't on here does not mean the program won't work**

### Operating Systems

* Linux (Ubuntu/Debian, may work on other distros)
* Windows 10 (WORK IN PROGRESS)

### CPUs
**Please note that while the module itself supports 32-bit and 64-bit architectures, the author only has access to a 64-bit test system.**

* AMD Ryzen 3/5/7 - Summit Ridge, Pinnacla Ridge, Raven Ridge, and Bristol Ridge CPUs
* AMD Bulldozer/Excavator - Probably works as well. 
* Intel - Kaby Lake and newer

No support for ARM cpus as of right now. 

# Installation (Ubuntu/Debian)

Please install the latest version of Python 3:

`sudo apt install python3`

or Python 2.7 if using v0.1:

`sudo apt install python2`

### Installing psutil

**Installing from Source**
**


**Installing with pip**
*NOTE: This version of psutil will only work with Python 2.7 - Will not work for v0.2 and above.*

Install pip, a Python package manager

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

`python get-pip.py`

Then install the psutil package with pip. 

`pip install psutil`


# Versions
### Current Versions

**v0.2** - Stable

### Previous Versions

**v0.1** - ~~Beta~~ Broken - Only works with Python2, utilizes different module ([PySensors](https://pypi.org/project/PySensors/)) as well.  
