# Netmiko: Connecting to Network Devices with Python

Netmiko is a Python library used to connect to network devices (like routers and switches) via SSH.  It simplifies the process of sending commands and retrieving output.

## Basic Connection Example

```python
# We will import "ConnectHandler" from the Netmiko module. ConnectHandler is used to specify connection parameters.
from netmiko import ConnectHandler

# Specify connection parameters for our R1 (which is a variable in Python)
R1 = ConnectHandler(ip = "10.8.102.10", username = "cisco", password = "cisco", secret = "cisco", device_type = "cisco_xe")

# Check the connection and print the connection status (True or False)
Check_R1 = R1.is_alive()
print("Connection to Router1:" + str(Check_R1))
# Output: True

# Disconnect from the router and print the connection status.
R1.disconnect()
Check_R1 = R1.is_alive()
print("Connection to Router1:" + str(Check_R1)) # Disconnected
# Output: False

```

## Command execution example

After establishing a connection, you can execute commands on the network device directly from your Python script.

### Checking the Prompt and Entering Enable Mode

```Python
# Check the current prompt
prompt = R1.find_prompt()
print(f"Current prompt: {prompt}")  # Example Output: Current prompt: R1>

# Enter enable mode
R1.enable()

# Check the prompt again
prompt = R1.find_prompt()
print(f"Prompt after enabling: {prompt}")  # Example Output: Prompt after enabling: R1#
```

### Send a list of configuration commands to the device and retrieve the output:

```Python
# List of configuration commands
commands = ["interface loop10", "description Created via PY", "ip address 111.111.111.111 255.255.255.255"]

# Send the configuration commands.  `send_config_set` automatically enters configuration mode.
output = R1.send_config_set(commands)
print(output)
# Example Output:
# config t
# interface loop10
# description Created via PY
# ip address 111.111.111.111 255.255.255.255
```


### Start SSH server on Windows 11 (Ubuntui WSL)
1. Start Ubuntu WSL

2. Start SSH service   
$ sudo service ssh start   
 *Starting OpenBSD Secure Shell server sshd*

3. Check SSH service status   
$ sudo service ssh status   
 *sshd is running*
