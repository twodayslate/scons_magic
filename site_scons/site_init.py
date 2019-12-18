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