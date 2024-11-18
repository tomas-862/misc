from netmiko import ConnectHandler  #
import textfsm


# Establish connections to the routers using their respective IP addresses and connection parameters.
R1 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5002")
R2 = ConnectHandler(ip="127.0.0.1", device_type="cisco_ios_telnet", port="5003")

# Define a list of devices containing the connection objects for easy iteration.
devices = [R1, R2]

def device_configs(dev):
    """Function to retrieve and print device hostname and interface statuses."""
    dev.establish_connection() # Establish a connection to the device
    dev.enable()  # Enter enable mode
    hostname = dev.send_command("show run | include hostname").split()[1]  # Get the hostname
    output = dev.send_command("show ip interface brief")  # Execute the command

    print(f"Connecting to device: {hostname}")

    # Open the TextFSM template file to parse the output
    with open("interface_brief.template") as temp:
        fsm = textfsm.TextFSM(temp) # Create a TextFSM object using the opened template
        result = fsm.ParseText(output) # Parse the output of the command
        print(fsm.header) # Print the header of the parsed results
        print(result)  # Print the structured output

    dev.disconnect()  # Disconnect from the device after the operations are complete
    print(f"Disconnected from device: {hostname}")  # Confirmation of disconnection

# Iterate over each device and retrieve configurations
for item in devices:
        device_configs(item) # Call the function for each device

