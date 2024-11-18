# Parse data from traceroute using 'TextFSM' 

# Trace from the router
traceroute = '''
Type escape sequence to abort.
Tracing the route to 192.168.3.1
VRF info: (vrf in name/id, vrf out name/id)
  1 192.168.12.2 0 msec
  2 192.168.23.3 4 msec
  3 192.168.3.1 0 msec
'''

import textfsm

# Open the template file and use it to parse data
with open("tracaroute.template.txt") as temp:
    fsm = textfsm.TextFSM(temp)
    # Properly parse the traceroute input
    result = fsm.ParseText(traceroute)

# Output the results
print(fsm.header)  # This should output: ['SEQ', 'NHOP']
print(result)      # This should output the parsed results




