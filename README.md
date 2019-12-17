Build /program (default)
```
scons
```

Build /program
```
scons build/program
```

Build multiple versions
```
scons build/program "build/program#platform@linux" "build/program#option@value"
```

When `platform@linux` is set the program will act differently - same with `option@value`!

The programs will be exported to export/
