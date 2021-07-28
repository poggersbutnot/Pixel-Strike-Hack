from pymem import Pymem, process
from requests import get
from webbrowser import open
from sys import exit

amt = 0
QIU = False #quit_if_update

print(get('https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/updates').text.replace('\n', ''))
ver = """1.0
"""
if ver != get('https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/version').text:
    print("New update available...")
    print("Update "+ get('https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hacks/main/version').text.replace('\n', '') + " is availible.")
    open("https://github.com/poggersbutnot/Pixel-Strike-Hack")
    if QIU is True:
        exit()
    else:
        pass
    if ver.replace('.', '') > get('https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/version').text.replace('.', ''):
        print("So u decided to change the version, but WHY.")
    else:
        pass
else:
    pass


pm = Pymem("PixelStrike3D.exe")
GameAssembly = process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

ammo = (0x1913212)
show = (0x233B720)
ban = (0x3AC5B70)
warn = (0x3ABF7B0)
ban2 = (0x3ABE450)
speedHackDetector = (0x3FA55D0)
time = (0x188ECC0)
# Bots only health = (0x2087C6A)


features = "Game time, Anti-Ban, Anti-Warn, Anti-Kick And incase that all failes, 0 ban time duration!"


class Main(object):

    @staticmethod
    def __init__():
        try:
            pm.write_int(GameAssembly + ammo, 10518783)
            if pm.read_int(GameAssembly + ammo) != 10518783:
               print("An error occured, retrying..."), pm.write_int(GameAssembly + ammo, 10518783)
            else:
               print("Infinite Ammo Added! Now Adding " + ''.join(features) + "... (Beta)."), pm.write_int(GameAssembly + show, 1465225360),
               pm.write_int(GameAssembly + ban, 242520208), pm.write_int(GameAssembly + warn, 136594631), pm.write_int(GameAssembly + ban2, 136594631),
               pm.write_int(GameAssembly + speedHackDetector, 136594631), pm.write_float(GameAssembly + time, -2.674721742E29) #, pm.write_float(GameAssembly + health, -13827.9873)
        except Exception:
            print("Please run PS3D before using this.")

        
        

Main()

