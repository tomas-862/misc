# This code establishes a connection to a Cisco router using Netmiko, 
# checks the connection status, and then disconnects. 


# We will import "ConnectHandler" from the Netmiko module. ConnectHandler is used to specify connection parameters.
from netmiko import ConnectHandler

# Specify connection parameters for our R1 (which is a variable in Python)
R1 = ConnectHandler(ip = "10.8.102.10", username = "cisco", password = "cisco", secret = "cisco", device_type = "cisco_xe")

# Check the connection and print the connection status (True or False)
Check_R1 = R1.is_alive()
print("Connection to Router1:" + str(Check_R1))

# Disconnect from the router and print the connection status.
R1.disconnect()
print("Connection to Router1: False") # Disconnected

