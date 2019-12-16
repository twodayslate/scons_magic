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

    env.PrependUnique(CPPPATH=[basePath])

    return i