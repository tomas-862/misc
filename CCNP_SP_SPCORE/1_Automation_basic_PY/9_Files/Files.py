# Change location to the directory of the file and print the current location and files in that directory.

import os

# Set the working directory
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/Files")

# Print the current working directory
print(os.getcwd())
print()

# Print the list of files in the current directory
print(os.listdir())
print()

# Open the configuration file "R1.cfg" in read-only mode
temp = open("R1.cfg", "r")

# Print the contents of the variable "R1_config"
R1_config = temp.read()
print(R1_config)

# This demonstrates how to read the content of the file.