
## TextFSM

**TextFSM** is an excellent tool for parsing data. While we can use **Regex** for parsing, **TextFSM** simplifies the process, as it was specifically designed to parse data from network devices.

### Example: Parsing Traceroute Data

Let's look at an example where we parse data from a router traceroute. Assume we have the following trace from our router:

```
R1#traceroute 192.168.3.1 probe 1
Type escape sequence to abort.
Tracing the route to 192.168.3.1
VRF info: (vrf in name/id, vrf out name/id)
  1 192.168.12.2 0 msec
  2 192.168.23.3 4 msec
  3 192.168.3.1 0 msec
```

In this case, we are interested only in the sequence numbers and the next hop IP addresses, along with the round-trip times in milliseconds (ms). We can use **TextFSM** to extract this information, obtain a structured output, and print it.

### Required Files

To utilize **TextFSM**, we need to create two files:
1. A **template** file, which can be saved with a `.txt` or `.fsm` extension.
2. A **Python script** file.

### Template File Content

For our example, the template file named `traceroute.template.txt` will have the following content:

```textfsm
Value SEQ (\d+)
Value NHOP (\S+)
Value MSEC (\d+ msec)

Start   
  ^\s*${SEQ}\s+${NHOP}\s+${MSEC} -> Record
```

### Python Script

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

# Sample output when running the script:
# > python3 .\TextFSM_trace.py
# ['SEQ', 'NHOP', 'MSEC']
# [['1', '192.168.12.2', '0 msec'], ['2', '192.168.23.3', '4 msec'], ['3', '192.168.3.1', '0 msec']]
# >
```