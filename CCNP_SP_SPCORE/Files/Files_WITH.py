# This script creates a list named "vlan1", which contains three dictionaries.
# Each dictionary represents a VLAN (Virtual Local Area Network) with a unique ID and name:
# - The first dictionary (index 0) includes VLAN ID 12 with the name "SERVER".
# - The second dictionary (index 1) includes VLAN ID 13 with the name "PC".
# - The third dictionary (index 2) includes VLAN ID 14 with the name "VOICE".
vlan1 = [{"id": "12", "name": "SERVER"}, {"id": "13", "name": "PC"}, {"id": "14", "name": "VOICE"}]

# The 'with' statement simplifies file operations, allowing us to create and write 
# the contents of the list "vlan1" to the "vlans1.cfg" file easily.

import os
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/Files")

# Open the file "vlans1.cfg" in write mode. 
# The 'with' statement ensures that the file is properly closed after the operations, 
# and allows for safe writing of VLAN configurations.
with open("vlans1.cfg", "w") as modify_vlans1:
    # Write the VLAN ID and name for the first VLAN to the file.
    modify_vlans1.write("vlan " + vlan1[0]["id"] + "\n")
    modify_vlans1.write("name " + vlan1[0]["name"] + "\n")
    
    # Write the VLAN ID and name for the second VLAN to the file.
    modify_vlans1.write("vlan " + vlan1[1]["id"] + "\n")
    modify_vlans1.write("name " + vlan1[1]["name"] + "\n")
    
    # Write the VLAN ID and name for the third VLAN to the file.
    modify_vlans1.write("vlan " + vlan1[2]["id"] + "\n")
    modify_vlans1.write("name " + vlan1[2]["name"] + "\n")

# This command will display the contents of the "vlans1.cfg" file in the terminal.
os.system("cat vlans1.cfg")
