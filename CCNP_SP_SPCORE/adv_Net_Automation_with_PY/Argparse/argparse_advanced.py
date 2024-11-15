# This Python script utilizes the Netmiko library to connect to two Cisco routers via Telnet. 
# It allows users to execute specific show commands on the routers and retrieve the corresponding outputs.


from netmiko import ConnectHandler
import argparse  # Importing the argparse module to handle command-line arguments

# Connect to routers
R1 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5002")
R2 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5003")

# Define the devices list containing the connection objects 
devices = [R1, R2]

# Creating an ArgumentParser object with a brief description
parser = argparse.ArgumentParser(description="container") 

# Adding positional arguments
parser.add_argument("show_cmd_1", help="Add first 'show' command you want to execute on the routers")
parser.add_argument("show_cmd_2", help="Add second 'show' command you want to execute on the routers") 

# Parsing the command-line arguments given by the user
args = parser.parse_args()

# Iterate over each device and execute the user-provided commands
for device in devices:
    print(f"Connecting to device {device.find_prompt()}")  # Display prompt for connection status
    # Entering privileged EXEC mode
    device.enable()
    prompt = device.find_prompt()
    print(f"Current prompt: {prompt}\n")

    # Execute the user input command
    device.send_command("terminal length 0")  # Changed from "ter len 0" to "terminal length 0" for clarity
    output_host = device.send_command("show running-config | include hostname")  # Check the hostname 
    hostname = output_host.split()[1].strip()  # Split the output and take the second element (index 1)
    print(f"This is the output of {hostname}: ")  # Print the hostname of the output 
    
    output_user1 = device.send_command(args.show_cmd_1)  # Sending user input 1 to router
    output_user2 = device.send_command(args.show_cmd_2)  # Sending user input 2 to router
    print("This is the output of the first show command:\n" + output_user1) 
    print()
    print("This is the output of the second show command:\n" + output_user2)
    print()

    # Disconnect from the device
    device.disconnect()