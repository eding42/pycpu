# PyCPU - A simple CPU monitoring tool

The `cpufreq` gnome extension freezing your computer? Can't find an alternative for CPU-Z on linux? Try `pycpu`, a simple and fast implementation of the psutil module!

The script outputs data about your system and CPU to your command line. 

Future GUI releases are planned. 

The `psutil` module was created by Giampaolo Rodola. 

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

* Linux (Ubuntu/Debian, should work on other distros with a little work)
* Windows 10 (WORK IN PROGRESS)
* ChromeOS - CPU Frequency broken, be sure you have all dependencies properly installed, as the Sandboxed linux present on Chromebooks lacks many key packages, like `build-essentials` for example. 

### CPUs
**Please note that while the original module itself supports 32-bit and 64-bit architectures, only 64 bit has been tested and developed.**

* AMD Ryzen 3/5/7 - Summit Ridge, Pinnacla Ridge, Raven Ridge, and Bristol Ridge CPUs
* AMD Bulldozer/Excavator - Probably works as well. 
* Intel - Kaby Lake and newer

No support for ARM cpus currently. 

# Installation (Ubuntu/Debian)

Please install the latest version of Python 3:

`sudo apt install python3`

or Python 2.7 if using v0.1:

`sudo apt install python2`

### Cloning the PyCPU git repository

**For Newest Version**

`git clone https://gitlab.com/eding42/pycpu.git`
`cd pycpu`

**For Specific Version (Stable)**

`git clone -b '<version-name>' --single-branch https://gitlab.com/eding42/pycpu.git git-<version-name>`

Replace `<version-name>` with the desirable version, ie `v0.2-Stable`.

### Installing psutil

**Installing from Source**

Clone the psutil git repo:

`git clone https://github.com/giampaolo/psutil.git`

`cd psutil`

Run the the psutil setup script:

`python3 setup.py install`

**Installing with pip**
*NOTE: This version of psutil will only work with Python 2.7 - Will not work for v0.2 and above.*

Install pip, a Python package manager

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

`python get-pip.py`

Then install the psutil package with pip. 

`pip install psutil`

If any permissions errors come up use `sudo`, or the `--user` tag.

**If there are any issues with installation, please refer to the Installation Issues section down below.**

# Versions
### Current Versions

Specific release notes are linked in the `tags` section of the repository.

**v0.2-Stable** - Adds finished CPU Frequency utility, adds a master script for controlling the daughter scripts. Beginnings of Temperature utility. 

### Previous Versions

*nothing here...*

# Known Issues

*Installer Script for psutil fails with error "ModuleNotFoundError: No module named 'distutils.core'"*

**Solution**

Make sure you have `distutils` and `pip` installed.

`sudo apt install python3-distutils`
`sudo apt install python3-pip`

Or if you want Python 2:

`sudo apt install python-disutils`
`sudo apt install python-pip`

*Installer Script for psutil fails with error "gcc: error: x86_64-linux-gnu-cc: No such file or directory"*

**Solution**

Make sure you have `build-essentials` installed.

`sudo apt install build-essentials`

Also make sure you have the `python3-dev` package installed

`sudo apt install python3-dev`