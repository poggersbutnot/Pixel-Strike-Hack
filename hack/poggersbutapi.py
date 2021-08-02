from requests import get
from pymem import Pymem, process

offsets = ([
    0x1913212,
    0x233B720,
    0x3AC5B70,
    0x3ABF7B0,
    0x3ABE450,
    0x3FA55D0,
    0x188ECC0,
    0xA13480,
    0x28B3687,
    0x28B3682,
    0x6AB66B,
    0x28B3717,
    0x28B3712
])


class MM(object):
    def __init__(
            self,
            ver: str = '1.6',
            app_name: str = 'PixelStrike3D',
            update_msg: str = get(
                'https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/info/updates').text.rstrip('\n')
    ):
        self.ver = ver
        self.update_msg = update_msg
        self.app_name = app_name
        self.pm = Pymem(self.app_name + '.exe')
        self.GameAssembly = process.module_from_name(self.pm.process_handle, "GameAssembly.dll").lpBaseOfDll

        print(update_msg)
        if ver != get(
                'https://raw.githubusercontent.com/poggersbutnot/Pixel-Strike-Hack/main/info/version').text.rstrip(
                '\n'):
            print("New version available.")
        else:
            pass

    def enable_ammo(self):
        return self.pm.write_int(self.GameAssembly + offsets[0], 10518783)

    def infinite_time(self):
        return self.pm.write_float(self.GameAssembly + offsets[6], -2.674721742E29)

    def infinite_bot_enemies(self):
        return [
            self.pm.write_float(self.GameAssembly + offsets[8], 3.335481139E10),
            self.pm.write_float(self.GameAssembly + offsets[9], 1.736125965E37)
        ]

    def rapid_fire(self):
        return self.pm.write_float(self.GameAssembly + offsets[10], -19.222)

    def infinite_friendly_bots(self):
        return {
            self.pm.write_float(self.GameAssembly + offsets[11], 3.335481139E10),
            self.pm.write_float(self.GameAssembly + offsets[12], 1.736125965E37)
        }

    @property
    def anti_cheat(self) -> [str, bytes]:
        return {
            self.pm.write_int(self.GameAssembly + offsets[1], 1465225360),
            self.pm.write_int(self.GameAssembly + offsets[2], 242520208),
            self.pm.write_int(self.GameAssembly + offsets[3], 136594631),
            self.pm.write_int(self.GameAssembly + offsets[4], 136594631),
            self.pm.write_int(self.GameAssembly + offsets[5], 136594631),
            self.pm.write_float(self.GameAssembly + offsets[7], 3.239628125E-29)
        }
