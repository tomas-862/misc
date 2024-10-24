# Create var of class dictionary "dic1" with key and value set (hostname, mgmt-ip, username, password)
# Create var of class dictionary "dic2" with key and value set (hostname, mgmt-ip, username, password)
# Create var of class dictionary "interface1" with key and value set (interface, ip_address)
# Create var of class dictionary "interface2" with key and value set (interface, ip_address)
# Create var of class list "data_center" with index 0 set as "dict1" and index 1 set as "dict2".
# Add / merge variable "interface1" to with "dict1" and "interface2" to with "dict2", so "interface1" will be nested to "dict1" and "interface2" with "dict2" Print it.


## with JSON we can perform more pretty print out, to visualise hierarfy of nested objects. 
## for this we will use json module in py and command "print(json.dump(data_center, ident=4))", 
## where "data_center" our variable and and index 4 ditance form the margins. 


# Import JSON and pretty print IP address of R1
# Import JSON and pretty print "data_center"



# Create var of class dictionary "dic1" with key and value set (hostname, mgmt-ip, username, password)
dict1 = {
    "hostname": "R1",
    "mgmt-ip": "10.1.1.1",
    "username": "tom",
    "password": "cisco"
}

# Create var of class dictionary "dic2" with key and value set (hostname, mgmt-ip, username, password)
dict2 = {
    "hostname": "R2",
    "mgmt-ip": "10.1.1.2",
    "username": "tom",
    "password": "cisco"
}

# Create var of class dictionary "interface1" with key and value set (interface, ip_address)
Interface1 = {
    "interface": "G1",
    "ip_address": "192.168.1.1"
}

# Create var of class dictionary "interface2" with key and value set (interface, ip_address)
Interface2 = {
    "interface": "G2",
    "ip_address": "192.168.1.2"
}

# Create var of class list "data_center" with index 0 set as "dict1" and index 1 set as "dict2". Print.
data_center = [dict1, dict2]
print(data_center)
print()

# Add / merge variable "interface1" to with "dict1" and "interface2" to with "dict2", so "interface1" will be nested to "dict1" and "interface2" with "dict2". Print. 
data_center [0]["interface"] = Interface1
data_center [1]["interface"] = Interface2
print(data_center)
print()

# Import JSON and pretty print IP address of R1
import json
print(json.dumps(Interface1, indent=4))

# Pretty print "data_center"
print(json.dumps(data_center, indent=4))

