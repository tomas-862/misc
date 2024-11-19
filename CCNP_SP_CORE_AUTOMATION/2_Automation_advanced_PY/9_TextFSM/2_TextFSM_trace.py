import textfsm  # Import the textfsm module for parsing text using FSM templates

# Trace from the router
traceroute = '''
Type escape sequence to abort.
Tracing the route to 192.168.3.1
VRF info: (vrf in name/id, vrf out name/id)
  1 192.168.12.2 0 msec
  2 192.168.23.3 4 msec
  3 192.168.3.1 0 msec
'''  # Define a multi-line string containing the output of the traceroute command

# Open the template file and use it to parse data
with open("traceroute.template.txt") as temp:  # Open the TextFSM template file
    fsm = textfsm.TextFSM(temp)  # Create a TextFSM object using the opened template

    # Properly parse the traceroute input
    result = fsm.ParseText(traceroute)  # Parse the traceroute string and store structured results in 'result'

# Output the results
print(fsm.header)  # Print the header of the parsed results (e.g., ['SEQ', 'NHOP', 'MSEC'])
print(result)      # Print the parsed results, which are the structured entries from the traceroute output
