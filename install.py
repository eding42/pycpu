import os

# Clone & Install psutil

print("\n------------------ Cloning 'psutil' ------------------\n")

os.system("git clone https://github.com/giampaolo/psutil.git")
os.chdir('psutil')

print("\n-------------- Installing Dependencies ---------------\n")

os.system("python3 setup.py install --user")
# This moves the working directory back up one layer.
os.chdir("..")
os.system("chmod +x pycpu.py")

print("\n------------------ Installation Finished! ------------------\n")