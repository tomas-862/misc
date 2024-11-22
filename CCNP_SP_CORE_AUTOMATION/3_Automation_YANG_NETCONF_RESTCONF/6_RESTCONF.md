# RESTCONF Protocol
Before RESTCONF, the existing methods (Telnet, SSH, SSL) were established and provided necessary security and control features not readily available through simple HTTP.

## Challenges with HTTP for Network Device Configuration

The use of plain HTTP for configuring network devices posed several challenges:
- **Security:** Plain HTTP transmits data in clear text, rendering it vulnerable to eavesdropping and manipulation. In contrast, Telnet and SSH offer encryption to safeguard sensitive configuration data.
- **Standardization:** There was no standardized method for representing network device configurations in a format easily interpretable by HTTP across various vendor equipment. RESTCONF addresses this issue by utilizing YANG data modeling.
- **Transaction Management:** Network configurations often demand atomic operations, where all changes succeed or none do. Standard HTTP lacks mechanisms to ensure transactional consistency, a need that NETCONF meets with its session-based approach.
- **Error Handling & Rollback:** Simple HTTP methods lack robust error handling and the functionality to roll back failed configuration changes.


## How RESTCONF Addresses These Issues
RESTCONF resolves the limitations of HTTP through several key features:
- **Using HTTPS:** Ensures secure communication.
- **Leveraging YANG:** Provides a standardized model for representing network device configurations.
- **Defining Specific HTTP Methods (GET, POST, PUT, PATCH, DELETE):** Maps CRUD operations to network configuration tasks.

## RESTCONF Commands

- **GET:** Retrieve operational or configuration data.
- **POST:** Create new resources.
- **PUT:** Update or replace existing resources.
- **PATCH:** Partially update existing resources.
- **DELETE:** Remove resources.

## Comparison: RESTCONF vs. NETCONF Commands

| **RESTCONF** | **NETCONF**                             |
|--------------|-----------------------------------------|
| GET          | `<get>`, `<get-config>`                |
| POST         | `<edit-config>` (operations="create")   |
| PUT          | `<edit-config>` (operations="create/replace") |
| PATCH        | `<edit-config>` (operations="merge")   |
| DELETE       | `<edit-config>` (operations="delete")  |

 RESTCONF offers a RESTful approach to network configuration but does not fully replace NETCONF in all scenarios. NETCONF's **stateful** nature is vital for complex configurations needing transactional consistency across multiple operations. While RESTCONF simplifies many interactions through its statelessness, this attribute can also limit its applicability in certain cases. For instance, in IOS-XR, configuration changes and commits must occur within a single session—an operation achievable via NETCONF but not RESTCONF. Thus, we can distinguish that NETCONF is stateful (maintains a session) while RESTCONF is stateless (does not maintain a session).
