# Define a list of VLANs with their IDs and names
import os

vlans = [
    {"id": "10", "name": "DATA"},
    {"id": "20", "name": "VOICE"},
    {"id": "30", "name": "MGMT"}
]

# Change the current working directory to the specified path (2)
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/Files")  # Navigate to the directory where the file will be created

# Open or create a new file named "vlans.cfg" in write mode
modify_vlans = open("vlans.cfg", "w")  # This creates an empty file named vlans.cfg if it doesn't already exist

# Write the contents of the "vlans" list to the "vlans.cfg" file
modify_vlans.write("vlan " + vlans[0]["id"] + "\n")  # Write VLAN ID for the first VLAN
modify_vlans.write("vlan " + vlans[0]["name"] + "\n")  # Write VLAN name for the first VLAN

modify_vlans.write("vlan " + vlans[1]["id"] + "\n")  # Write VLAN ID for the second VLAN
modify_vlans.write("vlan " + vlans[1]["name"] + "\n")  # Write VLAN name for the second VLAN

modify_vlans.write("vlan " + vlans[2]["id"] + "\n")  # Write VLAN ID for the third VLAN
modify_vlans.write("vlan " + vlans[2]["name"] + "\n")  # Write VLAN name for the third VLAN

# Save changes and close the file so that all data is written successfully
modify_vlans.close()

# Open the created vlans.cfg file in read mode to display its contents
temp = open("vlans.cfg", "r")  # Open the file for reading
SW_vlans = temp.read()  # Read the entire content of the file into the variable SW_vlans
print(SW_vlans)  # Print the contents of vlans.cfg to the console
