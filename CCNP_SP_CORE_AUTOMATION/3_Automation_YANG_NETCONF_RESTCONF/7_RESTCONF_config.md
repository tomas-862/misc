# RESTCONF Implementation

It is 99 percent similar to NETCONF, difference on the last step. 

## RESTCONF Configuration on Cisco IOS-XE

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

### 3. Enable RESTCONF
Enable the RESTCONF feature:
```plaintext
R1(config)# restconf
```

Now router is ready to recive REST API calls. 