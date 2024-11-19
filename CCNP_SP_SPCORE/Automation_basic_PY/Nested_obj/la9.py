# Import the JSON module for pretty printing
import json

# Create a dictionary variable "dic1" with key-value pairs: hostname, mgmt-ip, username, password
dic1 = {
    "hostname": "R1",
    "mgmt-ip": "10.1.1.1",
    "username": "tom",
    "password": "cisco"
}

# Create a dictionary variable "dic2" with key-value pairs: hostname, mgmt-ip, username, password
dic2 = {
    "hostname": "R2",
    "mgmt-ip": "10.1.1.2",
    "username": "tom",
    "password": "cisco"
}

# Create a dictionary variable "interface1" with key-value pairs: interface and ip_address
interface1 = {
    "interface": "G1",
    "ip_address": "192.168.1.1"
}

# Create a dictionary variable "interface2" with key-value pairs: interface and ip_address
interface2 = {
    "interface": "G2",
    "ip_address": "192.168.1.2"
}

# Create a list variable "data_center" with index 0 set to "dic1" and index 1 set to "dic2"
data_center = [dic1, dic2]

# Print the initial data_center list
print("Initial data_center:")
print(json.dumps(data_center, indent=4))  # Using JSON printing for readability
print()

# Nest "interface1" into "dic1" and "interface2" into "dic2"
data_center[0]["interface"] = interface1
data_center[1]["interface"] = interface2

# Print the updated data_center list with nested interfaces
print("Updated data_center with nested interfaces:")
print(json.dumps(data_center, indent=4))  # Pretty print the updated structure
print()

# Pretty print the details of "interface1"
print("Pretty printed interface1:")
print(json.dumps(interface1, indent=4))  # Displays interface1 in a readable format
print()

# Pretty print the entire "data_center" for a clear view of the hierarchy
print("Pretty printed data_center:")
print(json.dumps(data_center, indent=4))  # Visualizes the full structure of data_center
