# Script connects to a network device using Netmiko and applies OSPF configuration settings from a YAML file. 


import yaml
from netmiko import ConnectHandler

# Load the OSPF configuration from the YAML file
yaml_file = 'ospf.yaml'

# Safely open and parse the YAML file, extracting the OSPF configuration
with open(yaml_file, 'r') as file:
    ospf_config = yaml.safe_load(file)['ospf_configuration']

# Connect to the device using Netmiko with given connection details
device = ConnectHandler(ip = "127.0.0.1", device_type = "cisco_ios_telnet", port = "5002")

# Retrieve and print the current device prompt
prompt_device = device.find_prompt()
print(f"Current prompt: {prompt_device}")
print()


# Prepare OSPF configuration commands based on the YAML file
commands = [f'router ospf {ospf_config["process_id"]}']
for item in ospf_config['networks']:
    commands.append(f'network {item["network"]} {item["mask"]} area {item["area"]}')


# Apply the configuration commands to the device and print the output
output = device.send_config_set(commands)
print(output)


