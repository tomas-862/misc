import sys
from netmiko import ConnectHandler

# Connect to routers
R1 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5002")
R2 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5003")

# Define the devices list containing the connection objects
devices = [R1, R2]
args = sys.argv

command = sys.argv[1].strip().strip('"').strip("'")

# Iterate over each device and execute the user-provided command
for device in devices:
    print(f"Connecting to device {device.find_prompt()}")  # Display prompt for connection status
    device.enable()  # Enter privileged EXEC mode
    prompt = device.find_prompt()
    print(f"Current prompt: {prompt}")
    print()

    # Send commands and display output
    device.send_command("terminal length 0")  # Disable terminal paging
    output_host = device.send_command("show running-config | include hostname")  # Check the hostname 
    hostname = output_host.split()[1].strip()  # Split the output and take the second element
    print(f"This is the output of {hostname}: ")  # Print the hostname of the output 
    
    output_user = device.send_command(command)  # Sending the user input to the router
    print(output_user)  # Print the router's response to the command

    device.disconnect()  # Disconnect from the device