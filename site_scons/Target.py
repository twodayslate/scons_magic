import os
import sys
import platform
import SCons

defaultOptions = {
    "platform": sys.platform,
    "machine": platform.machine(),
    "architecture": platform.architecture()[0],
    "processor": platform.processor(),
    "docs": "True",
}

class Target:
    def __init__(self, name, options=None):
        global __defaultOptions
        self.name = name


        df = defaultOptions
        if options:
            self.options = options
            
            for key in df.keys():
                if key not in self.options:
                    self.options[key] = df[key]
        else:
            self.options = defaultOptions

    def path(self):
        ops = [os.path.split(self.name)[1]]
        for key in self.options.keys():
            val = key + "@" + self.options[key]
            val = val.lower().replace("/", '')
            ops.append(val)
        return "#".join(ops)

    def hasOption(self, option):
        try:
            self.options[option]
            return True
        except:
            return False

    def getOption(self, option, fallback=None):
        try:
            return self.options[option]
        except:
            return fallback

    def SConscript(self, exports=''):
        return SCons.Script.SConscript(dirs=[self.name], name="SConscript", exports=exports)