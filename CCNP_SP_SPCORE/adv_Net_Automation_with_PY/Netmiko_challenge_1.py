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
