# Solarium Project

## Overview
Solarium routes OpenVPN TCP traffic through `localhost:29977` using Stunnel to connect securely to a server. This document outlines how to set up the client and server configurations for Solarium.

## Client Setup
1. **Stunnel Configuration:**
   - Place the `stunnel.conf` file in the directory with your client configuration.
   
2. **OpenVPN Configuration:**
   - Add your own `solarium.ovpn` file to the same directory.
   - Modify the `solarium.ovpn` file to change the remote endpoint:
     ```
     remote 127.0.0.1 29988
     ```

## Server Setup
1. **Stunnel Server:**
   - Set up an Stunnel server listening on port 443.
   - Configure Stunnel to route the traffic to your OpenVPN TCP server, which typically listens on port 1194.

## Installation
- Run `install.bat` to install the necessary components. This script will set up desktop shortcuts and handle other necessary configuration steps automatically.

## Usage
After setting up both the client and server according to the instructions above, use the created desktop shortcuts to start the Solarium project. Ensure both Stunnel and OpenVPN services are running correctly.

## Support
For any issues or further configuration help, please refer to the project documentation or contact support.

