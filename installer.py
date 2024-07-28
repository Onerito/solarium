import os
import subprocess
from tqdm import tqdm
import time
import ctypes
import sys
import winshell
from win32com.client import Dispatch
# Check for admin privileges
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("Please run this script as an administrator.")
    sys.exit(1)

print("Running as administrator.\n")

logo = r'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,.,#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@..,......,,,.,,,,,**,,.,....,@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,......,.........*###/.................@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@.,,,,,....%@@@@@@@@&@@@@@@@@%@@@@@@@%.........,@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@.....,..&@@@@@@.......................@&@&@@@........@@@@@@@@@@@@@
@@@@@@@@@@@,,,....(@@@@&.........%&&@@@@@@@@@@@%.........&@@@@(...,,,.@@@@@@@@@@
@@@@@@@@@.......@@@&...... @@@@@@@#@@@@@&@@@@@@@@@@@@@(......@@@@..,.,,,@@@@@@@@
@@@@@@@,,....@@@&......@@@@&@&@@@@&@@@@.....(@@@&@@&&@%.,@......@@@@......@@@@@@
@@@@@@,,,,,&@@@ ....@@@&@@&@@@@@&@/....#@@@@@&@&@@@&@@@@@&@%. ....@@@#.....@@@@@
@@@@,.....@@@.....@@@&&@@@%@@&&& ...,@@&@@@@@@@&@&@&@@&&@&@&@&*.....@@@....,/@@@
@@@,,,,**@#@....@@@@&&@@@@@@@&.....@@@@@...........%@&&@&&&@@&@&.....@@@,,,,,,@@
@@,....*@@@....@(@@&&@@@@@@&. ...#@@&..................@&@@@@@@&&@....@@@*..../@
@@,,**,@@@....@@@@@@@@@&@@#. ....@@.....&&@@@@@@........,&&&&&@@&@#....@@%.....@
@...,.@&@....@@@@@@@&@@@@@@.....@@...@&@&.................&&%@@@@@@. ...@@@,,,,.
@,,,,,(@@...%@@@#@&@@@@&@@@.....@..@@@&@..................@&@&@@&@@.@..,(@@.....
,,,,,&@@....@@@@&@@@@@@@&&@.....@..@@@@*..................%&@@@@@@@.@....@@@....
.,,,.@@@....@@@@@@@@@@&@&%@........@&@&&............@.....&&@@&@&@,@@,,,,@@@*(((
,,,,,&@@....@@@&@@&&@&@&#@&@........@@@&&&........@&.....&&&@&&@@..@@....@@@,,.,
@,,,,,@@@,,./@@&@@@@&@&%%@@@@.........@@@&%&&@@@&@.....&@&@@&@@...@@....@@@..,,,
@,,,,,@@@....@@@@&@@@@@@&@@#&@.......,..............&@%@&@@@&...@@@@....@&@,,...
@@,,*,,@@@....@&@@@@&@@%@@@@&&@&..........%@@@%@@@@@@@@@@...../@@@@....&@@.....@
@@......@@@....@@@@@@@@@@@@@@&@&@& .........................@@@@@@.,,,@@@,,,**(@
@@@**,,,,@@@.....@&&&&@&@@@@&@&@@%&@@@ .................@@@@@@@@ ....@@@......@@
@@@@......@@@&..../@@@&@@&@@@@@&&@@&&@@@@@@@@@@@@@@@@&@@@@@@@@/....(@@@..,,,&@@@
@@@@@@,**,,,%@@*.....@@&@@@@&@@@&&@@@@@@@@@@@@@@&@@@@&@@@@@@......@@@......@@@@@
@@@@@@@,.,,,,,@@@@,..,..@&@&@@@@@&@&&@@&@@@@@@@@@@@@&@@@@(,..,.(@@@ ....,,@@@@@@
@@@@@@@@@,......@@@@(,,....,@@@@@@@@&@@@@@&@@@@@@@@@@#,.,..,,@@@@,.....,@@@@@@@@
@@@@@@@@@@@,,....,,@@@@@...,.,.,..&@@@@@&@@@@@@..........@@@@@,,,.,,,#@@@@@@@@@@
@@@@@@@@@@@@@@,*,,,,.,,@@@@@@#.,.,.,.............,.*@@@@@@*,,,,,,,,@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@,,,,**,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@*,,,,,.,,,,@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,,,.,,,,,,,,,,...,///.......,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@*,,,,,.......,////**,,,,,,,,%@@@@@@@@@@@@@@@@@@@@@@@@@

                     /$$                     /$$                        
                    | $$                    |__/                        
  /$$$$$$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$ /$$   /$$ /$$$$$$/$$$$ 
 /$$_____/ /$$__  $$| $$ |____  $$ /$$__  $$| $$| $$  | $$| $$_  $$_  $$
|  $$$$$$ | $$  \ $$| $$  /$$$$$$$| $$  \__/| $$| $$  | $$| $$ \ $$ \ $$
 \____  $$| $$  | $$| $$ /$$__  $$| $$      | $$| $$  | $$| $$ | $$ | $$
 /$$$$$$$/|  $$$$$$/| $$|  $$$$$$$| $$      | $$|  $$$$$$/| $$ | $$ | $$
|_______/  \______/ |__/ \_______/|__/      |__/ \______/ |__/ |__/ |__/
                                                                        
                                                                        
                                                                        
'''

for char in logo:
    print(char, end='', flush=True)
    time.sleep(0.0001)


def run(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")

installer_path = "stunnelinstallation.exe"

script_directory = os.path.dirname(os.path.abspath(__file__))

subprocess.run([installer_path, '/VERYSILENT'])

[time.sleep(0.1) for _ in tqdm(range(50))]

try:
    run("taskkill /f /im stunnel.exe")
except:
    print("Could not kill stunnel.exe as it was not running.")

[time.sleep(0.1) for _ in tqdm(range(15))]

print("Installing OpenVPN using msiexec...")
# Path to the MSI file
msi_path = "ovpn.msi"
if not os.path.isfile(msi_path):
    print(f"Error: {msi_path} not found.")
    sys.exit(1)

print("Checking if OpenVPN is already installed.")
# Check if OpenVPN is already installed
def is_openvpn_installed():
    return os.path.exists(r"C:\Program Files\OpenVPN\bin")

# Install OpenVPN using msiexec
if is_openvpn_installed():
    print("OpenVPN is already installed. Skipping installation.")
else:
    print("Installing OpenVPN using msiexec...")
    try:
        subprocess.run(["msiexec", "/i", msi_path, "/quiet", "/norestart", "/log", "msi_install.log"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


[time.sleep(0.1) for _ in tqdm(range(100))]

try:
    print("Killing OpenVPN GUI.")
    run("taskkill /f /im openvpn-gui.exe")
except:
    print("OpenVPN GUI process not found.")


# Create shortcuts

print("Creating shortcuts.")
# Function to create shortcuts
def create_shortcut(target, shortcut_path, icon_path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    shortcut.IconLocation = icon_path
    shortcut.save()

# Automatically get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Paths to the launch.bat and vanadium.ico
bat_file = os.path.join(script_directory, 'launch.bat')
icon_file = os.path.join(script_directory, 'icon.ico')
try:
    # Create shortcut on the Desktop
    desktop = winshell.desktop()
    desktop_shortcut = os.path.join(desktop, 'Solarium.lnk')
    create_shortcut(bat_file, desktop_shortcut, icon_file)

    # Create shortcut in the current directory
    current_directory_shortcut = os.path.join(script_directory, 'Solarium.lnk')
    create_shortcut(bat_file, current_directory_shortcut, icon_file)

    print("Shortcuts created successfully.")
except:
    print("Could not create shortcuts")

installedtext = r"""
 /$$                       /$$               /$$ /$$                 /$$
|__/                      | $$              | $$| $$                | $$
 /$$ /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$| $$  /$$$$$$   /$$$$$$$
| $$| $$__  $$ /$$_____/|_  $$_/   |____  $$| $$| $$ /$$__  $$ /$$__  $$
| $$| $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$| $$$$$$$$| $$  | $$
| $$| $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$| $$_____/| $$  | $$
| $$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$| $$|  $$$$$$$|  $$$$$$$
|__/|__/  |__/|_______/    \___/   \_______/|__/|__/ \_______/ \_______/

"""

for char in installedtext:
    print(char, end='', flush=True)
    time.sleep(0.005)

print("Make sure to read the README file if you haven't already!")


raspito = r'''

                                        /$$   /$$              
                                       |__/  | $$              
  /$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$ /$$$$$$    /$$$$$$ 
 /$$__  $$|____  $$ /$$_____/ /$$__  $$| $$|_  $$_/   /$$__  $$
| $$  \__/ /$$$$$$$|  $$$$$$ | $$  \ $$| $$  | $$    | $$  \ $$
| $$      /$$__  $$ \____  $$| $$  | $$| $$  | $$ /$$| $$  | $$
| $$     |  $$$$$$$ /$$$$$$$/| $$$$$$$/| $$  |  $$$$/|  $$$$$$/
|__/      \_______/|_______/ | $$____/ |__/   \___/   \______/ 
                             | $$                              
                             | $$                              
                             |__/                                                       

   .~~.   .~~.
  '. \ ' ' / .'
   .~ .~~~..~.
  : .~.'~'.~. :
 ~ (   ) (   ) ~
( : '~'.~.'~' : )
 ~ .~ (   ) ~. ~
  (  : '~' :  ) 
   '~ .~~~. ~'
       '~'
'''

for char in raspito:
    print(char, end='', flush=True)
    time.sleep(0.0033)

print("\nLaunch by clicking the desktop icon or the shortcut created in this directory and running as Administrator.")