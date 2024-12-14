# Task: Network Automation using Python

All routers have been pre-configured with IPv4 addressing and OSPFv2. To access the python interpreter, minimize the GNS3 application and open the terminal from the desktop. You may use ATOM as an editor for creating your scripts. All scripts should be stored in the pre-created folder "/root/Scripts". As a network engineer for INE, you have been assigned to automate the following tasks:

1. Create a script with the file name as **Lab1.py** which prints the following:

```code
show ip interface brief
show ip route | include 192.168.1.0
The password is "cisco"
This lab belongs to rome's class
```

2. Create a script with the file name as **Lab2.py**. Create a string variables named ccie1 which has the string value as CCIE EI. Create a string variables named ccie2 which has the string value as CCIE SP. Create a string variables named ccie3 which has the string value as CCIE SEC. Create a string variables named ccie4 which has the string value as CCIE DC. Create a integer type variables named ei which has the integer value as 40000. Create a integer type variables named sp which has the integer value as 10000. Create a integer type variables named sec which has the integer value as 15000. Create a integer type variables named dc which has the integer value as 5000. Print "There are 40000 CCIE EI certified people in the world". Print "There are 10000 CCIE SP certified people in the world". Print "There are 15000 CCIE SEC certified people in the world". Print "There are 5000 CCIE DC certified people in the world". Print "There are 70000 CCIE's in the world". Use the Format string feature to achieve this.

3. Create a script with the file name as **Lab3.py**. Create a string variables named old_ip_address1 which has the string value as 192.168.100.100. Create a string variables named old_ip_address2 which has the string value as 192.168.200.200. Use the split and replace built-in methods and replace all occurrences of .100 with .254. Use the split and replace built-in methods and replace the first occurrence of 200 with .254. Once the IP addresses are modified, print the following:

```code
The old IP addresses are 192.168.1.100 and 192.168.2.200
The new IP addresses are ['192', '168', 254, '254'] and ['192', '168', 254, '200']
```

4. Create a script with the file name as **Lab4.py**. Create a dictionary named dictionary1 with the following keys and values hostname": "R1", "mgmt-ip": "10.1.1.1", "username": "rohit", "password": "cisco". Create another dictionary named dictionary2 with the following keys and values hostname": "R2", "mgmt-ip": "10.1.1.2", "username": "rohit", "password": "cisco". Create another dictionary named interfaces_r1 with the following keys and values "interface1": "G1", "int1_ip_address": "192.168.1.1", "interface2": "G2", "int2_ip_address": "192.168.2.1". Create another dictionary named interfaces_r2 with the following keys and values "interface1": "G1", "int1_ip_address": "192.168.3.1", "interface2": "G2", "int2_ip_address": "192.168.4.1". Ensure the output below matches:

```code
print(json.dumps(data_center, indent=10))
[
          {
                    "hostname": "R1",
                    "mgmt-ip": "10.1.1.1",
                    "username": "rohit",
                    "password": "cisco",
                    "interfaces": {
                              "interface1": "G1",
                              "int1_ip_address": "192.168.1.1",
                              "interface2": "G2",
                              "int2_ip_address": "192.168.2.1"
                    }
          },
          {
                    "hostname": "R2",
                    "mgmt-ip": "10.1.1.2",
                    "username": "rohit",
                    "password": "cisco",
                    "interfaces": {
                              "interface1": "G1",
                              "int1_ip_address": "192.168.3.1",
                              "interface2": "G2",
                              "int2_ip_address": "192.168.4.1"
                    }
          }
]
```

5. Create a script with the file name as Lab5.py that loads the config from a file on R19 and R20. Create the configuration file and save it in the /root/Scripts folder. Router username is rohit and the password is admin. The file name and configuration to be loaded are given below:

R19.cfg

```code
router bgp 100
 neighbor 150.20.20.20 remote-as 100
 neighbor 150.20.20.20 update-source Loopback0
 end
write mem
```

```code
R20.cfg

router bgp 100
 neighbor 150.20.20.20 remote-as 100
 neighbor 150.20.20.20 update-source Loopback0
 end
write mem
```

6. Create a python script called as **Lab6.py** in the /root/Scripts. This script must accomplish the following:

- Ask for an input from the user, for example, “Enter the xe router show command you want to display?”
- Ask for an input from the user, for example, “Enter the xr router show command you want to display?”
- Ask for an input from the user, for example, “Enter the firewall show command you want to display?”
- Connect to each device (R19, R20, R21, XR11, ASA)
- Print the routing table
- Ensure the script asks for a username and password to connect to the devices.
- Router username is rohit and the password is admin.
- You must use a For Loop and a Function to achieve this task.

7. 
Create a python script called as **Lab7.py** in the /root/Scripts. This script must accomplish the following:

- Ask for the Username
- Ask for the Password
- Connect to each device in the topology and backup the configurations in the /root/Scripts folder.
- The backup must be stored in the format of hostname.cfg