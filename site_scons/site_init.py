__alreadyCalledInit = False
MY_CUSTOM_TARGETS = []
def CustomInit():
    global __alreadyCalledInit
    if __alreadyCalledInit:
        return
    __alreadyCalledInit = True

    global COMMAND_LINE_TARGETS
    global MY_CUSTOM_TARGETS
    global BUILD_TARGETS
    BUILD_TARGETS._clear()
    del BUILD_TARGETS[:]


    _targets = []
    for target in COMMAND_LINE_TARGETS:
        s = target.split("#")
        key = s[0]
        if key and key[0] != "#":
            _targets.append(key)

        values = {}

        t = Target(name=key)

        s = s[1:]
        if s:
            for sv in s:
                svv = sv.split("@")
                if len(svv) == 1:
                    values[svv[0]] = "True"
                else:
                    values[svv[0]] = svv[1]

        t = Target(name=key, options=values)
        MY_CUSTOM_TARGETS.append(t)

    COMMAND_LINE_TARGETS = []
    SCons.Script.COMMAND_LINE_TARGETS = []
    COMMAND_LINE_TARGETS = []

from Target import *

def Includes(name, env, inFolder="includes/"):
    """!
    Moves all header files for name to build/headers and
    adds build/sheaders to the include path
    """
    originPath = os.path.join(GetLaunchDir(), name, inFolder)
    files = Glob(os.path.join(originPath, '*.h'))

    basePath = os.path.join(GetLaunchDir(), "build", "headers")
    path = os.path.join(basePath, name)

    print("header files for", name, originPath, path, files)
    for f in files:
        print("\t", f.path)

    i = env.Install(path, files)
    Default(i)
    #env.Execute(i)
    #env.Alias('install', i)
    #env.Alias('implant', path)

    # TODO: add options
    #env.Execute(CopyHeaders("build/headers/" + name, files, env))

    #env.AppendUnique(CCFLAGS="-I" + )
    env.PrependUnique(CPPPATH=[basePath])

    return i