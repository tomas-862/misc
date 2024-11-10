# Install base hardware
total_routers = 50
total_switches = 100
total_firewalls = 10

# Calculate the total installed base of hardware
total_devices = total_routers + total_switches + total_firewalls

# Installed base software versions
router_version = "IOS-XE"
switch_version = "IOS 15.4"

# Number of IT engineers
it_engineers = 4

# Calculate workload per engineer
workload = total_devices / it_engineers

# Print results
print(f"My installed base is {total_devices} devices.")
print(f"Workload is {workload:.2f} devices per engineer.")
