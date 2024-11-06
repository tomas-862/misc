# we will create dictionary 
dict1 = {'hostname': 'R1', 'os': 'IOS-XE', 'mgmt-ip': '10.1.1.1'}
dict2 = {'hostname': 'R2', 'os': 'IOS-XR', 'mgmt-ip': '10.2.1.1'}

#we will create condition and action 
if dict1 ['os'] == 'IOS-XE':
    print(dict1['mgmt-ip'])

else:
    print("This device, not running 'IOS-XE'")
