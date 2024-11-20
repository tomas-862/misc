## YAML

- YAML (YAML Ain't Markup Language) is a human-readable data serialization format. You don’t need programming skills to understand or update a YAML file.

- Many high-level programming languages, such as Python, Perl, etc., can read and understand YAML files. In Python, you can import the YAML module to load a YAML file. This way, instead of embedding hundreds of device usernames and passwords in a Python script, you can store them in a YAML file and call them whenever needed.

- The YAML format has many similarities with JSON but offers features that make it more readable and writable for humans. While JSON is user-friendly in terms of output, its syntax can be less intuitive without programming knowledge.

- YAML is an excellent choice for configuration files and documentation where human interaction is necessary.

- YAML is compatible with many programming languages, providing cross-language compatibility.

- YAML structures data hierarchically, in a tree-like manner.

- You can use tags in YAML to indicate data types (e.g., lists).

- YAML supports comments, which is not possible in JSON.

**Let’s see some examples using a YAML file:**

1. **Creating a YAML file with a list of devices and connection information** - After creating this file, we will use it in a Python script to parse the connection information for connecting to devices.

### YAML file with a list of devices

```yaml
# List of devices
device_list:
  - hostname: router1
    ip: 127.0.0.1
    username: cisco
    password: cisco
    device_type: cisco_ios_telnet
    port: 5002
  - hostname: router2
    ip: 127.0.0.1
    username: cisco
    password: cisco
    device_type: cisco_ios_telnet
    port: 5003
```

### Python code to import a YAML file and print its contents as a Python dictionary

```python
# Import the YAML module for parsing YAML files
import yaml

# Define the path to the YAML file containing device information
yaml_file = 'devices.yaml'  # This variable holds the filename of the YAML file

# Open the specified YAML file in read mode
with open(yaml_file, 'r') as file:  # Using 'with' ensures the file is closed after reading
    # Load the contents of the YAML file safely and convert it into a Python dictionary
    devices = yaml.safe_load(file)  # safe_load is used to prevent the execution of any arbitrary code in the YAML

# Print the contents of the devices dictionary to the console
print(devices)  # This will display the parsed data from the YAML file
```
2. **Creating a YAML file that contains OSFP configuration** - After creating this file, we will use it in a Python script to parse the OSPF information and configure Network devices using parsed information.

### YAML file with OSPF configuration

```yaml
# OSPF configuration
ospf_configuration:
  process_id: 1
  networks:
    - network: 192.168.1.0
      mask: 0.0.0.255
      area: 0
    - network: 10.0.0.0
      mask: 0.0.255.255
      area: 0
```

### Python code to import a YAML file and send to network devices

```python
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

# Output:
# > python .\3_YAML_ospf.py
# Current prompt: R1#
#
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# R1(config)#router ospf 1
# R1(config-router)#network 192.168.1.0 0.0.0.255 area 0
# R1(config-router)#network 10.0.0.0 0.0.255.255 area 0
# R1(config-router)#end
# R1#
# PS C:\Users\tomas\OneDrive\Documents\Git\misc\CCNP_SP_CORE_AUTOMATION\2_Automation_advanced_PY\9_YAML_Jinja2>

```



