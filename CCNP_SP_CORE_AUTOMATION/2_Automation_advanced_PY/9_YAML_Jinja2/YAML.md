# YAML
- YAML is file format which are human readable format, you don’t need programming skills to understand and or update YAML file.   

- All high level programming languages like Python, Pear etc. can read and understand YAML file. In PY I can import YAML module in PY, then call YAML file in Python e.g. instead of having hundreds of devices usernames and password in PY script, I can have it in YAML file and call it whenever it needed.   

- YAML file format have many similarity with JSON but includes features which makes YAML file more readable and writable for humans. As JSON format print out is user friendly, but JSON script is not so easy to understand without programming knowledge.   

- YAML format is excellent choice for configuration files and documentation where human interaction is needed.   

- YAML is compatible with many languages i.e. cross language compatibility.   

- YAML is hierarchical format, tree-like manner.   

We can use tags, to indicate data types (lists etc.).   
- YAML supports comments (unlike JSON).   

**Let’s see some examples with YAML file:**
1. Lets create YAML file with list of device and information how to connect. After we will use this fle in PY script to parse connection inmformation to connect to devices. 

YAML file
```yaml
device_list:
- hostname: router1
- ip: 127.0.0.1
- username: cisco
- password: cisco


