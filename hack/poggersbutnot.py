from pymem import Pymem, process
from requests import post, get, put
from webbrowser import open
from sys import exit


QIU = False #quit_if_update

def announcments() -> str:
    return get('https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/info/updates').text.replace('\n', '')

print(announcments())
ver = """1.4
"""
verUrl = get('https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/info/version')

class UpdatesChecker(object):

    @staticmethod
    def __init__() -> str:
        global QIU
        try: 
            if ver != verUrl.text:
               print("New update available...")
               print("Update "+ verUrl.text.replace('\n', '') + " is availible.")
               open("https://github.com/poggersbutnot/Pixel-Strike-Hack")
               if QIU is bool(1):
                   exit()
               else:
                   pass
               if ver.replace('.', '') > verUrl.text.replace('.', ''):
                   print("So u decided to change the version, but WHY.")
               else:
                   pass
            else:
                pass
        except (Warning, Exception):
            print("An error occured.. ignoring.")

UpdatesChecker()

def is_outdated() -> [str, bool]:
    if get('http://pixelstrike3daws.com/new/version-info2.php', params = dict(platform=2, ver='8.9.0')).text == '{"ver":false,"msg":""}':
        return 'This program is outdated... wait for poggersbutnot (me) to make a update', True
    else:
        return 'PS3D version is up to date...', False

print(is_outdated()[0])

pm = Pymem("PixelStrike3D.exe")
GameAssembly = process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

ammo = (0x1913212)
show = (0x233B720)
ban = (0x3AC5B70)
warn = (0x3ABF7B0)
ban2 = (0x3ABE450)
speedHackDetector = (0x3FA55D0)
time = (0x188ECC0)
UpdatesChecker = (0x1718700)
WarningMenu = (0xA13480)
IncBots = (0x28B3687)
IncBots2 = (0x28B3682)
# Bots only health = (0x2087C6A)


features = "Game time, Anti-Ban, Anti-Warn, Anti-Kick And incase that all failes, 0 ban time duration!"


class Main(object):

    @staticmethod
    def __init__() -> str:
        try:
            pm.write_int(GameAssembly + ammo, 10518783)
            if pm.read_int(GameAssembly + ammo) != 10518783:
               print("An error occured, retrying..."), pm.write_int(GameAssembly + ammo, 10518783)
            else:
               print("Infinite Ammo Added! Now Adding " + ''.join(features) + "... (Beta)."), pm.write_int(GameAssembly + show, 1465225360),
               pm.write_int(GameAssembly + ban, 242520208), pm.write_int(GameAssembly + warn, 136594631), pm.write_int(GameAssembly + ban2, 136594631),
               pm.write_int(GameAssembly + speedHackDetector, 136594631), pm.write_float(GameAssembly + time, -2.674721742E29),
               pm.write_int(GameAssembly + UpdatesChecker, 136594631), pm.write_float(GameAssembly + WarningMenu, 3.239628125E-29),
               pm.write_float(GameAssembly + IncBots2, 1.736125965E37), pm.write_float(GameAssembly + IncBots, 3.335481139E10)  #, pm.write_float(GameAssembly + health, -13827.9873)
        except Exception:
            print("Please run PS3D before using this.")

        
        

Main()

