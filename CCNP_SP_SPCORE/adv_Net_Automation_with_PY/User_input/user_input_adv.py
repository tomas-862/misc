# import netmiko and os
from netmiko import ConnectHandler
import os


###### CREATE AND CHECK CONNECTIONS TO THE ROUTERS ######
# Create connection parameters for R1 and R2 (using device type linux as we don't have Cisco router for testing)
R1 = ConnectHandler(ip = "127.0.0.1", username = "cisco", password = "cisco", secret = "cisco", device_type = "linux")
R2 = ConnectHandler(ip = "172.29.47.175", username = "cisco", password = "cisco", secret = "cisco", device_type = "linux")

# Check connection to R1 and R2 and print connection status (expected status is True)
print("Checking connection")
Check_R1 = R1.is_alive()
Check_R2 = R2.is_alive()

print("Connection to Router1:" + str(Check_R1))
print("Connection to Router2:" + str(Check_R2))
print()


