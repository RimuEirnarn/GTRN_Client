"""A utility module"""
from os.path import exists


def fill(instance, index, content):
    """Filler to list/array.

    :type instance: list
    :type index: int
    :type content: Any
    :param instance: 'list' instance
    :param index: Index to be filled
    :param content: Content of a Index
    :return: None"""
    if isinstance(instance, list):
        instance_len = len(instance)
        if instance_len == index or instance_len > index:
            instance[index] = content
        if instance_len == index-1:
            instance.append(content)
        if instance_len < index:
            _n = index - instance_len
            for _n_ in range(_n+1):
                instance.append(None)
            instance[index] = content
        return None
    if isinstance(instance, dict):
        instance[index] = content
        return None
    else:
        raise TypeError("Instance need to be list")


def expect(instance, value, only_key=False):
    if isinstance(instance, list):
        if value in instance:
            return True
    if isinstance(instance, dict):
        _b = {}
        # Key is a repr and an Assignment. (instance['KEY'] = 'CONTENT'), but it will return
        # returns[KEY] = True
        # depending on keyword 'only_key'
        if only_key is False:
            for _a in instance:
                if value == instance[_a]:
                    _b[f"instance[{_a}]){value})"] = True
        else:
            for _a in instance:
                if value == _a:
                    _b[_a] = True
        return _b


def guess_os():
    """Guessing Operating That User used"""
    MSDOS = "C:\\"
    UNIX = "/usr/bin/python3"
    ANDROID = "/system/xbin"
    # Well i used some random path do define what OS They are
    # Support: Linux, MacOS. Android, Windows
    # There quite little chance that /data/media/0 is also on Other Linux
    # Beside Android
    # And these are random things and a common sense for OS-es
    if exists(MSDOS):
        return "Windows (MSDOS)"
    if exists(UNIX):
        if exists("/etc/os-release"):
            return open("/etc/os-release").readlines()[1].split("=")[1][1:-2]
        return "Linux/MacOS (UNIX)"
    if exists(ANDROID):
        return "Android (Linux)"
    if exists(UNIX) and exists(ANDROID):
        #TRY HARDER!
        ANDROID_PATH = ["/system/bin/sdcard", "/storage/self", "/data/user/0", "/data/misc/wifi", "/init"]
        EXISTANCES = []
        for _ANDROID in ANDROID_PATH:
            if exists(_ANDROID):
                EXISTANCES.append(True)
            else:
                EXISTANCES.append(False)
        del _ANDROID
        _b = 0
        for _a in EXISTANCES:
            _b += _a  # Since Boolean (True) is 1. so whatever
        if exists("/etc/os-release"):
            return open("/etc/os-release").readlines()[1].split("=")[1][1:-2]
        if _b == len(ANDROID_PATH):
            return "Android (Linux)"
        return "Android/Linux/MacOS (UNIX)"
