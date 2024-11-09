## Netmiko

Netmiko is python buidin module used to connect to router (via SSH) from python


We will import "ConnectHandler" from buildin module Netmiko. ConnectHandler is used to specify connection parameters.
```python
from netmiko import ConnectHandler
```

will specilfy connection parameters for our R1 (whcih is variable in py)
```python
R1 = ConnectHandler(ip = "10.8.102.10", username = "cisco", password = "cisco", secret = "cisco", device_type = "cisco_xe")
```

we can check connection, if it is connected and print if it is connected (True or False)
```python
Check_Connection_to_R1 = R1.is_alive()
```







