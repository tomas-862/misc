
# User Input in Python

In Python programming, the `input()` function is a fundamental tool used to gather input from the user. By default, this function captures the input as a string. To perform arithmetic operations, the string must be converted to an appropriate numerical type, such as an integer. Below, we'll explore a basic example of how to use this function, as well as a more advanced application involving network devices.

## Basic Example: User Input for Arithmetic Operations

We can utilize the `input()` function to prompt the user for information. In the example below, we ask the user to enter how many switches they have. Initially, the input is a string, but we convert it into an integer to perform mathematical operations:

```python
# Using the "input" function to obtain user input
switches = input("How many switches: ")
print(type(switches))  # Print the type of the variable
print()

# Convert the string to an integer
num_switches = int(switches)
print(type(num_switches))  # Print the type of the integer variable
print()

# Perform arithmetic operations, for instance, to calculate the number of interfaces (assuming each switch has 48 ports)
num_interfaces = num_switches * 48
print(f"There are a total of {num_switches} switches and a total of {num_interfaces} interfaces.")
print()
```

## Advanced Example: Using User Input with Network Devices

In a more complex example, we can leverage user input to interact with networking devices, such as to display the running configuration of a router. The following script establishes connections to simulated routers using Netmiko and allows the user to specify which router's routing table should be displayed based on their input:

```python
from netmiko import ConnectHandler
import os

#########################################################
###### CREATE AND CHECK CONNECTIONS TO THE ROUTERS ######
#########################################################
# Define connection parameters for R1 and R2 (using telnet for routers emulated in GNS3)

R1 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5002")
R2 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5003")

# Verify connections to R1 and R2 and print their status (expected status is True)
print()
print("Telnet connections to R1 and R2:")
Check_R1 = R1.is_alive()
Check_R2 = R2.is_alive()

print("Connection to Router1: " + str(Check_R1))
print("Connection to Router2: " + str(Check_R2))
print()

# Display the current command-line prompts
print("Current Prompts on R1 and R2:")
prompt_R1 = R1.find_prompt()
prompt_R2 = R2.find_prompt()

print(f"Current prompt: {prompt_R1}")  # Example Output: Current prompt: R1>
print(f"Current prompt: {prompt_R2}")  # Example Output: Current prompt: R2>
print()

#########################################################
###### GET USER INPUT ###################################
#########################################################
device = input("Which routing table do you want to check? ")

#########################################################
###### PROVIDE OUTPUT BASED ON USER INPUT ###############
#########################################################

if device.lower() == "r1":
    R1.enable()
    R1.send_command("ter len 0")
    print("This is the routing table of R1:")
    output = R1.send_command("show ip route")
    print(output)
    R1.disconnect()
elif device.lower() == "r2":
    R2.enable()
    R2.send_command("ter len 0")
    print("This is the routing table of R2:")
    output = R2.send_command("show ip route")
    print(output)
    R2.disconnect()
else:
    print("Invalid device")
```

In this script, user input determines which router's routing table is displayed. The script adjusts the terminal settings and retrieves the specified information accordingly, demonstrating a practical application of user input in a networking context.
