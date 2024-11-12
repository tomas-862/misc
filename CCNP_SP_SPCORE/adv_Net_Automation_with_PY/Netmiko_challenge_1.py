#########################################################
#########################################################
###### THIS IS NETMIKO CHALLENGE ########################
#########################################################
#########################################################

from netmiko import ConnectHandler
import os

#########################################################
###### CREATE AND CHECK CONNECTIONS TO THE ROUTERS ######
#########################################################
# Create connection parameters for R1 and R2 (using telnet as we emaulate routers on GNS3 and use telnet console)

R1 = ConnectHandler(ip = "127.0.0.1", device_type = "cisco_ios_telnet", port = "5002")
R2 = ConnectHandler(ip = "127.0.0.1", device_type = "cisco_ios_telnet", port = "5003")

# Check connection to R1 and R2 and print connection status (expected status is True)
print()
print("Telnet connections to R1 and R2:")
Check_R1 = R1.is_alive()
Check_R2 = R2.is_alive()

print("Connection to Router1:" + str(Check_R1))
print("Connection to Router2:" + str(Check_R2))
print()

# Check the current prompts
print("Current Promts on R1 and R2:")
prompt_R1 = R1.find_prompt()
prompt_R2 = R2.find_prompt()

print(f"Current prompt: {prompt_R1}")  # Example Output: Current prompt: R1>
print(f"Current prompt: {prompt_R2}")  # Example Output: Current prompt: R1>
print()

#########################################################
###### SAVE THE CONFIG FOR EACH ROUTER (WR MEM)    ######
#########################################################

# List of configuration commands
commands = "write memory"

# Send the configuration commands. 
output_wm_R1 = R1.send_command(commands)
print(f"Saving config for R1:\n{output_wm_R1}")
print()

output_wm_R2 = R2.send_command(commands)
print(f"Saving config for R2:\n{output_wm_R2}")
print()

#########################################################
###### SAVE CONFIG (SHOW RUN) to a CFG FILE        ######
#########################################################

# Change the current working directory to the specified path
os.chdir(r"C:\Users\tomas\OneDrive\Documents\Git\misc\CCNP_SP_SPCORE\adv_Net_Automation_with_PY")  # Navigate to the directory where the file will be created

# List of configuration commands
commands = "show run"

# Send the configuration commands. 
output_shr_R1 = R1.send_command(commands)
output_shr_R2 = R2.send_command(commands)

# Create a new file named "R1.cfg" and "R2.cfg" in write mode
with open("R1.cfg", "w") as modify_R1: # This creates or overwrites the file named R1.cfg if it doesn't already exist
    modify_R1.write(output_shr_R1)

with open("R2.cfg", "w") as modify_R2: # This creates or overwrites the file named R2.cfg if it doesn't already exist
    modify_R2.write(output_shr_R2)

# Check content of the files (optional). NOTE: Use "type" instead of "cat" as we run it on shell not bash. 
print("Content of .cfg files")
print()
os.system("type R1.cfg")
print()
os.system("type R2.cfg")
print()


#########################################################
###### DISCONNECTIONS FROM THE ROUTERS ###################
#########################################################
# Disconnect from R1 and R2 and check connection status
print("Telnet disconnections from R1 and R2:")
R1.disconnect()
R2.disconnect()

Check_R1 = R1.is_alive()
Check_R2 = R2.is_alive()

print("Connection to Router1:" + str(Check_R1))
print("Connection to Router23:" + str(Check_R2))
print()
