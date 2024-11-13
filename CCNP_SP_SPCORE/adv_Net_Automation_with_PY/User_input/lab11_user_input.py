import sys
from netmiko import ConnectHandler

# Connect to routers
R1 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5002")
R2 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5003")

# Define the devices list containing the connection objects
devices = [R1, R2]
prefix = "show "

# Initialize the attempt counter
n = 1 

# Continuously prompt for input until valid command is provided or max attempts reached
while n <= 5:  # Loop will run up to 5 times
    show_cmd = input("Which 'show' command to execute (must start with 'show ')? ")
    
    # Check if the command starts with the prefix
    if not show_cmd.lower().startswith(prefix):
        print("Invalid 'show' command, it must start with 'show '. Please try again.")
        n += 1  # Increment the attempt counter
    else:
        print("You entered a valid command.")
        print()
        break  # Exit the loop if a valid command is given

# If the maximum number of attempts is reached, exit the program
if n > 5:
    print("Maximum attempts reached. Terminating the request.")
    sys.exit()

# Iterate over each device and execute the user-provided command
for device in devices:
    print(f"Connecting to device {device.find_prompt()}")  # Display prompt for connection status
    # Entering privileged EXEC mode
    device.enable()
    prompt = device.find_prompt()
    print(f"Current prompt: {prompt}")
    print()

    # Execute the user input command
    device.send_command("ter len 0")
    output_host = device.send_command("show running-config | include hostname")  # check the hostname 
    hostname = output_host.split()[1].strip()  # Split the output and take the second element (index 1)
    print(f"This is the output of {hostname}: ")  # Print the hostname of the output 
    
    output_user = device.send_command(show_cmd) # Sending user input to router
    print(output_user) # Printing user input

    # Disconnect from the device
    device.disconnect()












