#########################################################
#########################################################
###### THIS IS NETMIKO CHALLENGE 2 ######################
####### !!! USE FOR LOOOP!!! ############################
#########################################################

# Importing modules
from netmiko import ConnectHandler
import os

# Change the current working directory to the specified path
os.chdir(r"C:\Users\tomas\OneDrive\Documents\Git\misc\CCNP_SP_SPCORE\adv_Net_Automation_with_PY")  # Navigate to the directory where the file will be created

#########################################################
###### CREATE AND CHECK CONNECTIONS TO THE ROUTERS ######
#########################################################
#########################################################
###### SAVE THE CONFIG FOR EACH ROUTER (WR MEM)    ######
#########################################################
#########################################################
###### SAVE CONFIG (SHOW RUN) to a CFG FILE        ######
#########################################################
#########################################################
###### DISCONNECTIONS FROM THE ROUTERS ##################
#########################################################

# Create connection parameters for R1 and R2 (using telnet as we emaulate routers on GNS3 and use telnet console)
R1 = ConnectHandler(ip = "127.0.0.1", device_type = "cisco_ios_telnet", port = "5002")
R2 = ConnectHandler(ip = "127.0.0.1", device_type = "cisco_ios_telnet", port = "5003")


# Check connection, save config, save to file and disconnect (for loop)
devices = [R1, R2]
n = 1

for device in devices:
    # Check if the device connection is alive
    print("Connecting to Device") 
    if device.is_alive(): 
        print("Device R" + str(n) + " is connected")

    # Entering privileged EXEC mode
    print("Move to privileged EXEC mode") 
    device.enable() 
    prompt = device.find_prompt()
    print(f"Current prompt: {prompt}")

    # Saving the configuration
    print("Saving the config")
    device.send_command("write memory")

    # Writing the device config to file
    print("Backing up config to .cfg file")
    device.send_command("terminal lenght 0")
    device_config = device.send_command("show running-config")
    with open(f"R_{n}.cfg", "w") as temp:
        temp.write(device_config)

    # Disconnect from device
    device.disconnect()
    print(f"Disconnected from Device R{n}")
    
    n = n + 1 # Increment index for naming files

