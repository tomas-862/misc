# This script connects to routers R1 and R2 to retrieve the routers' hostname,
# their software version, and all interface names along with their IP addresses.

from netmiko import ConnectHandler  # Importing the ConnectHandler class from the Netmiko library, which is used to establish SSH/Telnet connections to network devices.
import re  # Importing the regular expressions module to facilitate pattern matching in strings.

# Establish connections to the routers using their respective IP addresses and connection parameters.
R1 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5002")
R2 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5003")

# Define a list of devices containing the connection objects for easy iteration.
devices = [R2, R1]

# Define a function 'get_hostname' to fetch the hostname of the connected device.
def get_hostname(dev):
    dev.enable()  # Enter enable mode on the device to access privileged commands.
    # Execute the command to retrieve the hostname, split the output, and extract the hostname.
    hostname = dev.send_command("show run | inc hostname").split()[1]  # 'split()[1]' extracts the hostname from the output.
    print("Device " + hostname)
    return hostname  # Return the hostname for potential use in other functions.

# Define a function 'get_version' to retrieve the software version of the connected device.
def get_version(dev):
    dev.enable()  
    software = dev.send_command("show version")  # Execute the command to retrieve the software version details.
    pattern = re.compile(r"Version (\S+)")  # Compile a regex pattern to match the version string.
    version_match = pattern.search(software)  # Search the output for a version string match.

    if version_match:  # Check if a match was found in the version output.
        print("Software version " + version_match.group(1))
    else:
        print("Software version not found") 



# Iterate through the list of devices to call the defined functions and process each router.
for device in devices:
    print("############################")
    get_hostname(device)  # Call the function to get and print the hostname of the current device.
    print("############################")
    print("############################")
    get_version(device)  # Call the function to get and print the software version of the current device.
    print("############################")
    print()
    device.disconnect()  # Disconnect from the device after processing to free up resources.


