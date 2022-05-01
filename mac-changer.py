import optparse
import subprocess
from rich.console import Console
import re
import time
from tempita import sub

parser = optparse.OptionParser()
console = Console()
banner = ('''
[#8509f2]
=================================================================
 [rgb(255,0,255)]
   __  __               _____ _
  |  \/  |             / ____| |
  | \  / | __ _  ___  | |    | |__   __ _ _ __   __ _  ___ _ __
  | |\/| |/ _` |/ __| | |    | '_ \ / _` | '_ \ / _` |/ _ \ '__|
  | |  | | (_| | (__  | |____| | | | (_| | | | | (_| |  __/ |
  |_|  |_|\__,_|\___|  \_____|_| |_|\__,_|_| |_|\__, |\___|_|
                                                 __/ |
                                                |___/
                                              
[#8509f2]
=================================================================

                    [#8eed35]
                     Author =>
                         __
                        (_ |_  _ |_ . _
                        __)| )(_||_)||

                    Version =>
                            2.0[#8509f2]
=================================================================

''')
success = ('''
                                                          
[rgb(255,0,255)]
        ___________  _________________________________
        __  ___/  / / /  ___/  ___/  _ \_  ___/_  ___/
        _(__  )/ /_/ // /__ / /__ /  __/(__  )_(__  ) 
        /____/ \__,_/ \___/ \___/ \___//____/ /____/  
                                                    
          
                                              
''')


def macChanger(interface, mac):
    console.print(banner, style="blue")
    time.sleep(2)
    console.print(
        f"[#8eed35][+] Changing Mac Address of Interface {interface} to {mac}")
    time.sleep(2)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def getMac():
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change Mac Adress")
    parser.add_option("-m", "--mac", dest="mac",
                      help="Mac Adress you want to set")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("\033[1;31;49m Please enter the interface or -h for help")
    elif not options.mac:
        parser.error("\033[1;32;49m Please Enter Mac to Change or -h for help")
    return options


def getCurrentMac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    final_mac = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if final_mac:
        return final_mac.group(0)
    else:
        print("Mac  Not FOund")


options = getMac()
user_mac = getCurrentMac(options.interface)
console.print(
    f'''[green]
    ========================================================================

           [#8eed35] Device Current Mac For {options.interface} is =[red] {str(user_mac)}[green]
    
    =========================================================================
    ''')
macChanger(options.interface, options.mac)

user_mac = getCurrentMac(options.interface)
if user_mac == options.mac:
    console.print(success)
    console.print(f'''[green]
    ===================           =====================      ===================
    ===       [#8eed35]  Mac Adress Successfully Change To [red]{options.mac}[green]          ===          
    ===================           ======================     ====================
    ''')
else:
    console.print('''
    [  [red]Mac Adress Not Change ]
     ''')
