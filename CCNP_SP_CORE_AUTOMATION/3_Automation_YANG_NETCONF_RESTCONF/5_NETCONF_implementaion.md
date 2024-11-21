# NETCONF Implementation
NETCONF is designed to be utilized by software applications rather than manually edited by users. Manually crafting XML can be quite challenging, so it's generally best to use a NETCONF controller (e.g., Cisco DNA Center or similar) that leverages NETCONF under the hood.

### Key Points
- With Cisco IOS that supports NETCONF, a global session lock is available.
- NETCONF can be manually invoked for testing and laboratory purposes using various tools:
  - **Postman**
  - **Python (PY)**
  - **cURL** (Linux command line tool)
  - **Terminal Window**
However, as mentioned, most use cases will involve a NETCONF controller, and manually executing commands is not common practice.

## NETCONF Configuration on Cisco IOS-XE

### 1. Create a Self-Signed Trustpoint (if not existing)
Enable the HTTPS server by executing the following command:
```plaintext
R1(config)# ip http secure-server
% Generating 1024 bit RSA keys, keys will be non-exportable...[OK]
Failed to generate persistent self-signed certificate.
Secure server will use temporary self-signed certificate.

*Nov 21 22:30:14.631: %SSH-5-ENABLED: SSH 1.99 has been enabled
R1(config)#
```

### 2. Configure Username/Password with Level 15 Access
Create a username with administrative privileges:
```plaintext
R1(config)# username cisco privilege 15 password cisco
```

### 3. Enable NETCONF-YANG
Enable the NETCONF-YANG feature:
```plaintext
R1(config)# netconf-yang
```

### 4. (Optional) Change the Default NETCONF Port (Default is 830)
If needed, change the NETCONF port to a different value:
```plaintext
R1(config)# netconf-yang ssh port <1-65535>
```

## NETCONF Monitoring on Cisco IOS-XE

### 1. Check NETCONF Sessions
To view current NETCONF sessions:
```plaintext
R1# show netconf-yang session
R: Global-lock on running datastore
C: Global-lock on candidate datastore
R: Global-lock on startup datastore

Number of sessions: 3

Session ID       User              Source IP        Status       Global Lock 
-------------------------------------------------------------------------------
1                 admin            192.168.1.100    Active       R: Global-lock on running datastore
2                 operator         192.168.1.101    Active       C: Global-lock on candidate datastore
3                 user1            192.168.1.102    Idle         R: Global-lock on startup datastore
```
From the above output, we can observe the global lock status.

### 2. Check Supported Datastores

To check which datastores the device supports:
```plaintext
R1# show netconf-yang datastores

Datastore Information:
-----------------------------------------------------------------------------------
| Datastore             | Status               | Lock Type              | Lock Owner          |
-----------------------------------------------------------------------------------
| running               | Active               | R: Global-lock         | admin               |
| startup               | Inactive             | RW: None               | N/A                 |
| candidate             | Active               | C: Global-lock         | operator            |
-----------------------------------------------------------------------------------

Total Datastores: 3
```
