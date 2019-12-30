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

        self.originalTargetString = None

    def path(self) -> str:
        ops = [os.path.split(self.name)[1]]
        for key in self.options.keys():
            val = key + "@" + self.options[key]
            val = val.lower().replace("/", '')
            ops.append(val)
        return "+".join(ops)

    def uniqueName(self) ->str:
        return str(hex(hash(self.path()))).replace('0x', self.name+'_').replace('-','')

    def variantDir(self) -> str:
        '''
        The build directory
        '''
        return os.path.join("#/build", self.path())
    buildDir = variantDir

    def exportDir(self):
        return os.path.join("#/export", self.path())

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

    def SConscript(self, exports=None):
        if exports == None:
            exports = []
        if isinstance(exports, list):
            exports.append('self')
        elif isinstance(exports, str):
            exports = exports + ' self'
        elif isinstance(exports, dict):
            exports['self'] = self
        return SCons.Script.SConscript(os.path.join(SCons.Script.GetLaunchDir(), self.name, 'SConscript'), variant_dir=self.variantDir(), exports=exports)

def PARSE_TARGET(target: str) -> Target:
    try:
        s = target.split("+")
        key = s[0]
        name = key
        values = {}

        s = s[1:]
        if s:
            for sv in s:
                svv = sv.split("@")
                if len(svv) == 1:
                    values[svv[0]] = "True"
                else:
                    values[svv[0]] = svv[1]
        options = values
    except:
        name = target
        options = None

    t = Target(name=name, options=options)
    t.originalTargetString = target
    return t
