#  install base HW
Total_routers = 50
Total_swithces = 100
Total_firewalls = 10

# calculate my install base HW
Total_devices = Total_routers + Total_swithces + Total_firewalls

#  intall base SW 
Router_version = "IOS-XE"
Switch_version = "IOS 15.4"

# FTE resourse
IT_engineers = 4

# calculate work load 
Work_load = Total_devices / IT_engineers

print("my install base is", Total_devices, "devices")
print("work load is", Work_load,"devices per engineer")