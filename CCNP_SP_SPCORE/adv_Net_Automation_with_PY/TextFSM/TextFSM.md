## TextFSM

'TextFSM' is a great way to parsing data. We did it with 'Regex', but it is easier to parse data using 'TextFSM' as it was created to parse data from Network devices. 

Lets check one example, where we will parse data from traceroute. Assume we have atrace:   

R1#traceroute 192.168.3.1 probe 1
Type escape sequence to abort.
Tracing the route to 192.168.3.1
VRF info: (vrf in name/id, vrf out name/id)
  1 192.168.12.2 0 msec
  2 192.168.23.3 4 msec
  3 192.168.3.1 0 msec

Lets assume we need only sequence number and next hop IP address. We can use 'TextFSM' to parse the data, get structured output and print it. 

NOTE: Using 'TextFSM' we will have 2 files, 1 files will be .py our scrips and another file will be our parsed output. 

```python

