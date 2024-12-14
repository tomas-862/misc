# Create a script with the file name as Lab4.py. 


# Create a dictionary named dictionary1 with the following keys and values hostname": "R1", "mgmt-ip": "10.1.1.1", "username": "rome", "password": "cisco". 
# Create another dictionary named dictionary2 with the following keys and values hostname": "R2", "mgmt-ip": "10.1.1.2", "username": "rome", "password": "cisco". 
# Create another dictionary named interfaces_r1 with the following keys and values "interface1": "G1", "int1_ip_address": "192.168.1.1", "interface2": "G2", "int2_ip_address": "192.168.2.1". 
# Create another dictionary named interfaces_r2 with the following keys and values "interface1": "G1", "int1_ip_address": "192.168.3.1", "interface2": "G2", "int2_ip_address": "192.168.4.1". 
# Ensure the output below matches:
#[
#          {
#                    "hostname": "R1",
#                    "mgmt-ip": "10.1.1.1",
#                    "username": "rome",
#                    "password": "cisco",
#                    "interfaces": {
#                              "interface1": "G1",
#                              "int1_ip_address": "192.168.1.1",
#                              "interface2": "G2",
#                              "int2_ip_address": "192.168.2.1"
#                    }
#          },
#          {
#                    "hostname": "R2",
#                    "mgmt-ip": "10.1.1.2",
#                    "username": "rome",
#                    "password": "cisco",
#                    "interfaces": {
#                              "interface1": "G1",
#                             "int1_ip_address": "192.168.3.1",
#                              "interface2": "G2",
#                              "int2_ip_address": "192.168.4.1"
#                    }
#          }
#]

import json

dictionary1 = {
    "hostname" : "R1",
    "mgmt-ip" : "10.1.1.1",
    "username" : "rome",
    "password" : "cisco"
}
dictionary2 = {
    "hostname" : "R2",
    "mgmt-ip" : "10.1.1.2",
    "username" : "rome",
    "password" : "cisco"
}
interfaces_r1 = {
    "interface1": "G1", 
    "int1_ip_address": "192.168.1.1", 
    "interface2": "G2", 
    "int2_ip_address": "192.168.2.1" 
}
interfaces_r2 = {
    "interface1": "G1", 
    "int1_ip_address": "192.168.3.1", 
    "interface2": "G2", 
    "int2_ip_address": "192.168.4.1"
}

# The data_center list combines these two dictionaries.
data_center = [dictionary1, dictionary2] 

# Interface configurations are added as a new key to each device's dictionary.
data_center[0]["interfaces"] = interfaces_r1 # [0] point to 1st dictionary in the list 
data_center[1]["interfaces"] = interfaces_r2 # [0] point to 2nd dictionary in the list 


pretty_json = json.dumps (data_center, indent=4)

print(pretty_json)