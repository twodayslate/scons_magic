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

    lookupFolder(os.path.join(target.platform))
    lookupFolder(os.path.join(target.platform, target.arch))
    lookupFolder(os.path.join(target.platform, target.arch, target.bits))
    
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

        paths = [originPath]

        paths = [os.path.join(GetLaunchDir(), _source, inFolder, _target.platform)] + paths
        paths = [os.path.join(GetLaunchDir(), _source, inFolder, _target.platform, _target.arch)] + paths
        paths = [os.path.join(GetLaunchDir(), _source, inFolder, _target.platform, _target.arch, _target.bits)] + paths

        _env.PrependUnique(CPPPATH=paths)

    AddMethod(Environment, Include)

    def ImportLibrary(
        _env, _target, _source, *args, **kwargs
    ):
        _env.Include(_target, _source, *args, **kwargs)
        newTarget = Target(_source, _target.platform, _target.arch, _target.bits)
        newTarget.parent = _target
        i = SConscript(dirs=[os.path.join("#", _source)], variant_dir=os.path.join('#/build', _target.path(), _source), exports={'self': newTarget})
        return i

    AddMethod(Environment, ImportLibrary)

    return env