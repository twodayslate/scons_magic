import os
import sys
import platform
import SCons


class Target:
    def __init__(self, name, platform=sys.platform, arch=platform.machine(), bits=platform.architecture()[0].replace('bits',''), parent=None):
        self.name = name
        self.platform = platform
        self.arch = arch
        self.bits = bits
        self.parent = parent

    def path(self):
        return "_".join([self.name, self.platform, self.arch, self.bits])

    def variant_dir(self):
        '''
        The build directory
        '''
        return os.path.join('#/build', self.path())

    def export_dir(self):
        return os.path.join('#/export', self.path())