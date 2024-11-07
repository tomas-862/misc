#1 Create a variable of class dict named "dict1" which contains a key and value set as:
## {"hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"}

#2 Create a variable of class dict named "dict2" which contains a key and value set as:
## {"hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}

#3 Create a function named "device_ip" to display the following management IP of the device. 
## The management IP must be displayed based on the following conditions:
### If OS is IOS-XE, then print "The management IP of {hostname} is {mgmt-ip}."
### If OS is IOS-XR, then print "The management IP of {hostname} is {mgmt-ip}."
### If OS is NEXUS, then print "This device has an unknown image."

#4 Save the function as Lab_Func_Cond.py

#5 Ensure you are able to call this function by importing it using the command "from Lab_Func_Cond import device_ip."

#1 and 2 
def device_ip(temp):
       dict1 = {"hostname": "R1", "OS": "IOS-XE", "mgmt-ip": "10.1.1.1"}
       dict2 = {"hostname": "R2", "OS": "IOS-XR", "mgmt-ip": "10.1.1.2"}
       if temp == "IOS-XE":
        print(f"The management IP of {dict1['hostname']} is {dict1['mgmt-ip']}")
       elif temp == "IOS-XR":
        print(f"The management IP of {dict2['hostname']} is {dict2['mgmt-ip']}")
       else:
        print("This device has a unknown image")
    
#5 

# we go to Python, and from here import funcion from our file
## >>> from Lab_Func_Cond import device_ip
## >>>
## >>>
## >>>
## >>> device_ip("IOS-XE")
## The management IP of R1 is 10.1.1.1
## >>> device_ip("IOS-")
## This device has a unknown image
## >>> device_ip("IOS-HR")
## This device has a unknown image
## >>>