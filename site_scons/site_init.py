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

    def ImportLibrary(
        _env, _target, _source, *args, **kwargs
    ):
        _env.Include(_target, _source, *args, **kwargs)
        newTarget = Target(name=_source, options=_target.options)
        newTarget.parent = _target
        self = newTarget
        i = SConscript(dirs=[os.path.join("#", _source)], variant_dir=os.path.join('#/build', _target.path(), _source), exports=['self'])
        return i

    AddMethod(Environment, ImportLibrary)

    return env