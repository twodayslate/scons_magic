import os
import sys
import platform
import SCons

validPlatforms = ['darwin', 'aix', 'linux', 'win32', 'cygwin']
validArch = ['i386','x86_64','arm']
validBits = ['32', '64']

def PARSE_TARGET(target):
    _target = target.replace('#/build', '').replace('build','').replace('/','')
    s = _target.split("_")
    _platform = sys.platform
    _arch = platform.machine()
    _bits = platform.architecture()[0].replace('bit','')
    name = s[0]
    try:
        options = s[1:]
        for s in options:
            if s in validPlatforms:
                _platform = s
            elif s in validArch:
                _arch = s
            elif s in validBits:
                _bits = s
            else:
                print("Invalid target option '%s'"  % s)
                SCons.Script.Exit(1)
    except:
        pass
    t = Target(name, _platform, _arch, _bits)
    t.parsedTarget = target

    return t

class Target:
    def __init__(self, name, platform=sys.platform, arch=platform.machine(), bits=platform.architecture()[0].replace('bit',''), parent=None):
        self.name = name
        self.platform = platform
        self.arch = arch
        self.bits = bits
        self.parent = parent
        self.parsedTarget = None

    def path(self):
        return "_".join([self.name, self.platform, self.arch, self.bits])

    def variant_dir(self):
        '''
        The build directory
        '''
        return os.path.join('#/build', self.path())

    def export_dir(self):
        return os.path.join('#/export', self.path())