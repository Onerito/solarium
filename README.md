# Solarium Project

### Note
This was **not** intended as a commercial project, it was just made for me and my friends. However in the end I just decided to post it to github for others to use. This was not made with intent to be used for others and doesn't have a server setup file, but it just makes the entire process easier especially for non tech savvy people.

## Overview
Solarium routes OpenVPN TCP traffic through `localhost:29988` using Stunnel to connect securely to a server. This document outlines how to set up the client and server configurations for Solarium. A local listening port is made on port 29988 which OpenVPN connects to. The traffic sent into that port is sent outbound over port 443 after being encrypted to appear as normal HTTPS traffic. About 99% of firewalls that allow web browsing, this will evade. No dependencies are required, as it is all contained as an installer. Run INSTALL.BAT to install it. It creates 2 shortcuts, one on the desktop and one in the solarium directory which can be located anywhere just cant be deleted. The shortcut must be ran as administrator but can also be changed in the properties to automatically run as admin.

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

