# PyCPU - A simple CPU monitoring tool

The `cpufreq` gnome extension freezing your computer? Can't a good CPU monitor on linux? Try `pycpu`, a simple and fast implementation of the psutil module!

The script outputs sensor data about your system and CPU to the command line. 

Future GUI releases are planned. 

The `psutil` module was created by Giampaolo Rodola. 

# Functionality and Features
### Current Features

1. CPU Frequency - Stable (MHz)

2. CPU Temperature - Stable, around 80% done. 

### Planned Features

3. CPU Utilization (%) - Planned

4. CPU Core Count - Planned

5. CPU Advanced Stats (CTX Switches, Interrupts, etc) - Planned

A. Curses implementation planned and in development. 

# Supported Systems
**Please note that this list is far from exhaustive. pycpu should still work with any reasonably up to date system, provided architectural requirements are fulfilled.**

### Operating Systems

* Linux (Ubuntu/Debian, should work on other distros with a little work)
* Windows 10 - Planned
* ChromeOS - CPU Frequency and other sensors most likely broke. Missing many dependencies. 

### CPUs
**Please note that while the original module itself supports 32-bit and 64-bit architectures, only 64 bit has been tested and developed.**

* AMD Ryzen 3/5/7 or AMD Family 17h  - Zen and Zen2-based architectures Summit Ridge(Zen), Pinnacle Ridge(Zen+), Raven Ridge(Zen), Matisse(Zen2) 
* AMD Threadripper - Probable support.
* AMD Bulldozer/Excavator or AMD Family 15h - Bristol Ridge CPUs and older. Bulldozer support is currently unverified. 
* Intel Core - Skylake and Derivatives. All except for Kaby Lake untested. 

No support for ARM processors.

# Installation (Ubuntu/Debian)

## Dependencies

Please install the latest version of Python 3 and the associated -dev package:

`sudo apt install python3 python3-dev`

or Python 2.7 if using v0.1 and below:

`sudo apt install python2 python-dev`

### Cloning the PyCPU git repository

**For Stable Version**

`git clone https://gitlab.com/eding42/pycpu.git`

`cd pycpu`

Run the installer script, which will install all necessary dependencies. 

`python3 install.py`

**For Legacy Releases**

A list of previous versions can be found under the 'Tags' section of Github.

`git clone -b '<version-name>' --single-branch https://gitlab.com/eding42/pycpu.git git-<version-name>`

Replace `<version-name>` with the desired version, ie `v0.2-Stable`.

### Installing psutil

**Installing from Source**

Clone the psutil git repo:

`git clone https://github.com/giampaolo/psutil.git`

`cd psutil`

Run the the psutil setup script:

`python3 setup.py install`

If user permission errors are encountered, run the `--user` tag instead. 

`python3 setup.py install --user`

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

**v1.0-Stable** - Version v1.0 has been released! All bugs on the CPU Frequency branch and most on the CPU Temperature branch have been worked through. Both sides are currently functional. 

### Previous Versions

**v0.2-Stable** - Adds finished CPU Frequency utility, adds a master script for controlling the daughter scripts. Beginnings of Temperature utility. 

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
