
# YANG Model

## Introduction

YANG (Yet Another Next Generation) is a data modeling language that provides a standardized way to define configuration and state data in network devices. Its emergence addresses the limitations of previous models, such as MIBs (Management Information Bases) used with SNMP (Simple Network Management Protocol), by offering a more flexible and robust method for managing network configurations.

## History of MIB and SNMP

- **MIB**: MIBs were initially developed to facilitate the management of network devices via SNMP. They define the structure of the management data of a device and use a hierarchical namespace to access the data.

- **SNMP**: SNMP, which has dominated network management for decades, relies on MIBs to access and manipulate device settings and performance metrics. However, SNMP primarily operates at a scalar level and lacks the structured approach required for complex configurations.

### Limitations of MIB and SNMP

1. **Complex Hierarchies**: MIBs can become unwieldy when modeling complex interdependencies and nested data structures.
  
2. **Vendor-specific Models**: Different vendors implement their own MIBs, leading to fragmentation and compatibility issues across devices from various manufacturers.

3. **Human-Centric**: MIBs and SNMP were designed with humans as the primary users, making them less suited for automated processes and machine interactions.

## YANG: A New Approach

YANG was developed to provide a more coherent and flexible framework for modeling network configurations. Here are some key features:

### Key Features of YANG

- **Container and Leaf Constructs**: YANG allows for the creation of containers that can hold multiple leaf elements. For example:
  ```plaintext
  container device {
      leaf name {
          type string;  // Device name
      }
      leaf type {
          type boolean; // Indicates if the device is active
      }
  }
  ```

- **Modular Design**: YANG models support modularity, enabling reuse of definitions and components across different models.

- **Hierarchical Structure**: YANG utilizes a hierarchical structure that makes it easier to represent complex configurations in a logical and organized manner.

- **Data Types**: YANG supports various data types (e.g., integers, strings, Booleans) which allow for precise definition of the data structure, improving validation and error checking.

- **Constraints and Validation**: YANG allows for the inclusion of constraints (e.g., ranges, patterns) directly in the model to ensure that data complies with certain rules.

- **Extensibility**: New features or enhancements can be added to YANG models without breaking existing implementations, allowing for future compatibility and growth.

- **Standardization and Governance**: 
  - YANG models come from various sources. Companies often create their own proprietary models, referred to as **Native Models** or **Vendor Models**.
  - Organizations like the **IETF (Internet Engineering Task Force)** work to standardize models for wider acceptance.
  - Consortiums, such as **OpenConfig**, aim to create vendor-agnostic models that can be utilized across multiple platforms.

- **Documentation Support**: YANG provides constructs for embedding documentation within the model, facilitating easier understanding and usage of the data structures.

### Preloaded Model Support

One of the advantages of YANG is that these models do not need to be downloaded to devices manually. Manufacturers pre-download the supported YANG models. Vendors determine which YANG models to support based on their device capabilities and market requirements. 

## Cisco YANG Models

Cisco provides a comprehensive set of YANG models for its devices, which can be found in their GitHub repository at the following link: [Cisco YANG Models on GitHub](https://github.com/YangModels/yang/tree/main/vendor/cisco/xe).

### Description of the Repository

In the Cisco repository:
- **Vendor-Specific Models**: The models are designed to represent various configurations and operational states for Cisco's software and hardware platforms.
- **Hierarchical Structure**: Models are organized hierarchically, allowing easy navigation and understanding of device capabilities.
- **Examples and Documentation**: The repository includes examples and documentation to help users understand how to implement and use the models in their network automation and management tasks.

By utilizing these models, network engineers can automate configurations, monitor states, and ensure consistency across their Cisco devices, enhancing network assurance and operational efficiency.

## PYANG: A Tool for Working with YANG Models

**PYANG** is a command-line tool that helps network engineers read, analyze, and validate YANG files. It enhances the usability of YANG by providing several important features:

- **Validation**: PYANG can validate YANG modules against the YANG specification, ensuring that models are syntactically correct.
