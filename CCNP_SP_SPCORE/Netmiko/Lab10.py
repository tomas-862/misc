# import Netmiko
from netmiko import ConnectHandler

# will create connection parameters for R1 amd R2 (will use device type linux as we don't have cisco router for tesing)
R1 = ConnectHandler(ip = "127.0.0.1", username = "cisco", password = "cisco", device_type = "linux")

R2 = ConnectHandler(ip = "172.29.47.175", username = "cisco1", password = "cisco1", device_type = "linux")

# Check connection to R1 and R2 and print connection status (expected status is True)
print("checking connection")
Check_R1 = R1.is_alive()
print("Connection to Router1:" + str(Check_R1))

Check_R2 = R2.is_alive()
print("Connection to Router1:" + str(Check_R2))


# Disconnect from R1 and R2. Check connection to R1 and R2 and print connection status (expected status is True)
print("checking disconnection")
R1.disconnect()
R2.disconnect()

Check_R1 = R1.is_alive()
print("Connection to Router1:" + str(Check_R1))

Check_R2 = R2.is_alive()
print("Connection to Router1:" + str(Check_R2))