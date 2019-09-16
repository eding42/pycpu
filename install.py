import os
import subprocess

# Abort function.
def abort():
   print("Error occurred. Aborting now...\n")
   os._exit(0)

# Checks for existing dependencies 
print("\n--------------- Checking for Dependencies ---------------\n")

# Checks for the build-essential package
x=subprocess.call("dpkg -s build-essential", shell=True)
if x == 1:
   print("\nYou still have to install build-essential package. \n\nPlease run 'sudo apt install build-essential'\n")
   abort()

# Checks for the setup-tools package
try:
   import setuptools
except ImportError:
   print("Please install the python3-setuptools package")

# Checks for the installation of the python3-dev package.
x=subprocess.call("dpkg -s python3-dev", shell=True)
if x == 1:
   print("\nYou still have to install the python3-dev package. \n\nPlease run 'sudo apt install python3-dev'\n")
   abort()

# Clone & Install psutil

print("\n------------------ Cloning 'psutil' ------------------\n")

os.system("git submodule add https://github.com/giampaolo/psutil.git")
os.chdir('psutil')

print("\n-------------- Installing Dependencies ---------------\n")

os.system("python3 setup.py install --user")
# This moves the working directory back up one layer.
os.chdir("..")
os.system("chmod +x pycpu.py")

print("\n------------------ Installation Finished! ------------------\n")
