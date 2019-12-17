from Target import *

def SpecialGlob(target, path, inFolder=''):
    originalFiles = Glob(os.path.join(inFolder, path))
    files = originalFiles

    def lookupFolder(folder):
        #print("looking in ", os.path.join(inFolder, folder, path))
        newFiles = Glob(os.path.join(inFolder, folder, path))
        for f in newFiles:
            print(f)
            replace = False
            for (i, orig_f) in enumerate(files):
                if os.path.splitext(f.name)[0] == os.path.splitext(orig_f.name)[0]:
                    print("Replacing", orig_f.name, "with", f.name)
                    files[i] = f
                    replace = True
                    break
            if not replace:
                files.append(f)

    for firstKey in target.options.keys():
        firstPath = firstKey + "@" + target.options[firstKey]
        firstPath = firstPath.lower().replace('/', '')
        lookupFolder(firstPath)
        for secondKey in target.options.keys():
            secondPath = secondKey + "@" + target.options[secondKey]
            secondPath = secondPath.lower().replace('/', '')
            if secondPath == firstPath:
                continue
            lookupFolder('+'.join([firstPath, secondPath]))
            for thirdKey in target.options.keys():
                thirdPath = thirdKey + "@" + target.options[thirdKey]
                thirdPath = thirdPath.lower().replace('/', '')
                if thirdPath == secondPath:
                    continue
                if thirdPath == firstPath:
                    continue
                lookupFolder('+'.join([firstPath, secondPath, thirdPath]))
    print("files for ", target.name, ":")
    for f in files:
        print("\t", f.path)
    return files


def SpecialEnvironment():
    env = Environment()
    def Include(
        _env, _target, _source, inFolder="includes/", *args, **kwargs
    ):
        originPath = os.path.join(GetLaunchDir(), _source, inFolder)
        files = SpecialGlob(_target, '*.h', inFolder=originPath)

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