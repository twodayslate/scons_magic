from Target import *

def SpecialEnvironment():
    env = Environment()
    def Include(
        _env, _target, _source, inFolder="includes/", *args, **kwargs
    ):
        originPath = os.path.join(GetLaunchDir(), _source, inFolder)
        files = Glob(os.path.join(originPath, '*.h'))

        basePath = os.path.join('#/build', _target.path(), "headers")
        path = os.path.join(basePath, _source)

        print("header files for", _source, originPath, path, files)
        for f in files:
            print("\t", f.path)

        i = _env.Install(path, files)
        Default(i)

        _env.PrependUnique(CPPPATH=[basePath])

        return i

    AddMethod(Environment, Include)

    return env