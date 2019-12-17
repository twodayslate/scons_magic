import SCons

SCons.Script.Main.AddOption('--verbose',
  dest='verbose',
  action='count',
  help='Set verbosity level. Default: 0')

def DebugPrint(p, *args, **kwawrgs):
    if SCons.Script.Main.GetOption('verbose') and SCons.Script.Main.GetOption('verbose') > 0:
        print(p, *args, **kwargs)