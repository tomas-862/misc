
# Define devices under "device_info" funcion and define list of all devices under "device_list"
def device_info(os):
    dev1 = {"hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"}
    dev2 = {"hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}
    dev3 = {"hostname": "R3", "OS": "IOS-XE", "mgmt-ip": "10.1.1.3"}
    dev4 = {"hostname": "R4", "OS": "IOS-XR", "mgmt-ip": "10.1.1.4"}
    dev5 = {"hostname": "R5", "OS": "NEXUS", "mgmt-ip": "10.1.1.5"}
    device_list = [dev1, dev2, dev3, dev4, dev5]

# Loop through each device in device_list
    for device in device_list:
        os_type = device["OS"]
        hostname = device["hostname"]
        mgmt_ip = device["mgmt-ip"]

        if os_type == os:
            print(f"The management IP of {hostname} running {os_type} is {mgmt_ip}")
        else:
            pass

# Run the function (change argument as needed)
device_info("IOS-XE")