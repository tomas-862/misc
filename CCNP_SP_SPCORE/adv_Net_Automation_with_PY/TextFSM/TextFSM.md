## TextFSM

'TextFSM' is a great way to parsing data. We did it with 'Regex', but it is easier to parse data using 'TextFSM' as it was created to parse data from Network devices. 

Lets check one example, where we will parse data from router traceroute. Assume we have follow trace on our router:   

R1#traceroute 192.168.3.1 probe 1
Type escape sequence to abort.
Tracing the route to 192.168.3.1
VRF info: (vrf in name/id, vrf out name/id)
  1 192.168.12.2 0 msec
  2 192.168.23.3 4 msec
  3 192.168.3.1 0 msec

Lets assume we need only sequence number and next hop IP address with ms. We can use 'TextFSM' to parse the data, get structured output and print it.   

NOTE: Using 'TextFSM' we will have to create two files:   
1. So called 'teamplate' file, which can be .txt or .fsm text file.   
2. .py scrips file.    

In our example template file with name 'traceroute.template.txt' will have follow content:   


**Value SEQ (\d+)**
**Value NHOP (\S+)**
**Value MSEC (\d+ msec)**

**Start**
  **^\s*${SEQ}\s+${NHOP}\s+${MSEC} -> Record**



```python
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

# Output:
# > python3 .\TextFSM_trace.py
# ['SEQ', 'NHOP', 'MSEC']
# [['1', '192.168.12.2', '0 msec'], ['2', '192.168.23.3', '4 msec'], ['3', '192.168.3.1', '0 msec']]
# >
# 
```
