import subprocess
import os
import ctypes
import sys
import time
from tqdm import tqdm
# Check for admin privileges
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("Please run this script as an administrator.\n")
    sys.exit(1)
def run(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")


launchtext = r'''
                     /$$                     /$$                        
                    | $$                    |__/                        
  /$$$$$$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$ /$$   /$$ /$$$$$$/$$$$ 
 /$$_____/ /$$__  $$| $$ |____  $$ /$$__  $$| $$| $$  | $$| $$_  $$_  $$
|  $$$$$$ | $$  \ $$| $$  /$$$$$$$| $$  \__/| $$| $$  | $$| $$ \ $$ \ $$
 \____  $$| $$  | $$| $$ /$$__  $$| $$      | $$| $$  | $$| $$ | $$ | $$
 /$$$$$$$/|  $$$$$$/| $$|  $$$$$$$| $$      | $$|  $$$$$$/| $$ | $$ | $$
|_______/  \______/ |__/ \_______/|__/      |__/ \______/ |__/ |__/ |__/
                                                                        
                                                                        
                                                                        
 /$$                                         /$$       /$$                    
| $$                                        | $$      |__/                    
| $$  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$$| $$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
| $$ |____  $$| $$  | $$| $$__  $$ /$$_____/| $$__  $$| $$| $$__  $$ /$$__  $$
| $$  /$$$$$$$| $$  | $$| $$  \ $$| $$      | $$  \ $$| $$| $$  \ $$| $$  \ $$
| $$ /$$__  $$| $$  | $$| $$  | $$| $$      | $$  | $$| $$| $$  | $$| $$  | $$
| $$|  $$$$$$$|  $$$$$$/| $$  | $$|  $$$$$$$| $$  | $$| $$| $$  | $$|  $$$$$$$
|__/ \_______/ \______/ |__/  |__/ \_______/|__/  |__/|__/|__/  |__/ \____  $$
                                                                     /$$  \ $$
                                                                    |  $$$$$$/
                                                                     \______/ 
                                                                     
...............,,,::::::::;;;::,,,,...............
...........,,,:::::;+***??**++;::::,,,............
.........,::::;*?SSS%%???*??%%SSS%*;:::,,.........
.......,:::+?SS%*;;:;;++++++;;;;+*%SS?+:::,.......
.....,:::+S#%+::+?%S##@@@@##SS%%?+;:+?#S*:::,.....
...,:;:+S#*::+%##@@@@#S?**??%SSSSS%?+::*#S+::,....
...:::?@%:,+S@@###@#?;:*S#@@@@@@@@@##?:,:%@?:::,..
..:;;?@*,:%@@####@%:,;S@#%?***?S#@##@@#*,,*@%:;:..
.:;:?@?,;S@#####@?,,+#%+::::::::;*#@##@@%:,*@?:::.
,;;+@S::%@#####@S,::S*,+?%?*+;;::,;%####@+,:%@+::,
:::%@+,+@@#####@*,:+?:%@S+:::::::::;####@%;:+@%::,
;;;##::%@######@*::;+*@@*,::::::;:::S@##@?%::S#:::
;:;#S::S@#######?,:::*@@%:,,,,,;*:::S@#@S*S::S#+++
;;;##;:%@########;,:::?#@#?*+*??;,;%@@@S;S%::##;;:
:;:%@+:+@@########;,:::;*%SS%?+:;?#@#S*:%@+,+@%:::
,;;;#S::%@#######@#*:,,::;+**?%S##%?+:;S@%::S@;::,
.:;:*@?::%@@########S*;:,,:::;;;::::+%@@%::?@?;;:.
.,:::*@%::*#@#######@@#S?*+;;;;+*?S#@@#*::?@*:::,.
...:;:*#S+,;%#@####@###@@@@@@@@@@@@@@%;,;S#+:::,..
...,:;:;%#%;:;?S#@@@@@#####@@@@@@@#%+:;?#%;:::....
.....,:::+%#S*;:;*%S##@@@@@@@#S%?+::+%#S+:::,.....
.......,:::;?S#S?+;;;;++++++;;;;+*%#S?+;::,.......
.........,:;;;+*%SSSS%%?????%SSSS%*+;:::,.........
...........,,:::::;++***???***+;;;:::,............
...............,,,::,::;;;;;;:::,,,...............
'''
for char in launchtext:
    print(char, end='', flush=True)
    time.sleep(0.00043)

run("taskkill /f /im stunnel.exe")

[time.sleep(0.02) for _ in tqdm(range(100))]

script_directory = os.path.dirname(os.path.abspath(__file__))

subprocess.Popen(r'''"C:\Program Files (x86)\stunnel\bin\stunnel.exe" ''' + f"\"{script_directory}\\stunnel.conf\"")

[time.sleep(0.1) for _ in tqdm(range(100))]

# Path to OpenVPN executable
openvpn_path = r"C:\Program Files\OpenVPN\bin\openvpn.exe"

# Automatically get the directory of the script
cwd_directory = os.getcwd()

# Path to the OpenVPN configuration file
config_path = os.path.join(cwd_directory, 'solarium.ovpn')

# Command to execute with a space before '--config'
openvpn_command = f'"{openvpn_path}" --config "{config_path}"'


subprocess.run(openvpn_command, shell=True, check=True)