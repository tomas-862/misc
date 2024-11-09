# import netmiko and os
from netmiko import ConnectHandler
import os


###### CREATE AND CHECK CONNECTIONS TO THE ROUTERS ######
# will create connection parameters for R1 amd R2 (will use device type linux as we don't have cisco router for tesing)
R1 = ConnectHandler(ip = "127.0.0.1", username = "cisco", password = "cisco", device_type = "linux")
R2 = ConnectHandler(ip = "172.29.47.175", username = "cisco1", password = "cisco1", device_type = "linux")

# Check connection to R1 and R2 and print connection status (expected status is True)
print("Checking connection")
Check_R1 = R1.is_alive()
Check_R2 = R2.is_alive()

print("Connection to Router1:" + str(Check_R1))
print("Connection to Router2:" + str(Check_R2))
print()


###### CREATE .CFG FILES FOR THE ROUTERS ######
# Change the current working directory to the specified path
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/Netmiko")  # Navigate to the directory where the file will be created

# Define R1 and R2 parameters
R1_parameters = [{"host": "Router1", "RP": "router ospf 1", "RID": "1.1.1.1", "default": "0.0.0.0 255.255.255.255 area 0"}] 
R2_parameters = [{"host": "Router2", "RP": "router ospf 1", "RID": "2.2.2.2", "default": "0.0.0.0 255.255.255.255 area 0"}] 

# Create a new file named "R1.cfg" and "R2.cfg" in write mode
with open("R1.cfg", "w") as modify_R1: # This creates an empty file named R1.cfg if it doesn't already exist
    modify_R1.write(R1_parameters[0]["host"] + "\n")
    modify_R1.write(R1_parameters[0]["RP"] + "\n")
    modify_R1.write(R1_parameters[0]["RID"] + "\n")
    modify_R1.write(R1_parameters[0]["default"] + "\n")
    
with open("R2.cfg", "w") as modify_R2: # This creates an empty file named R2.cfg if it doesn't already exist
    modify_R2.write(R2_parameters[0]["host"]["RP"]["RID"]["default"])
    modify_R2.write(R2_parameters[0]["host"] + "\n")
    modify_R2.write(R2_parameters[0]["RP"] + "\n")
    modify_R2.write(R2_parameters[0]["RID"] + "\n")
    modify_R2.write(R2_parameters[0]["default"] + "\n")

# check content of the files
print("Content of .cfg files")
os.system("cat R1.cfg")
os.system("cat R1.cfg")
print()








# Disconnect from R1 and R2. Check connection to R1 and R2 and print connection status (expected status is True)
print("Checking disconnection")
R1.disconnect()
R2.disconnect()

Check_R1 = R1.is_alive()
Check_R2 = R2.is_alive()

print("Connection to Router1:" + str(Check_R1))
print("Connection to Router23:" + str(Check_R2))

