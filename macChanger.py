import optparse
import subprocess
from rich.console import Console

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
                            1.0[#8509f2]
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
    console.print(
        f"[#8eed35][+] Changing Mac Address of Interface {interface} to {mac}")
    console.print(
        f"[#8eed35]Successfully change Mac adress to {mac} {success}")
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


options = getMac()
macChanger(options.interface, options.mac)
