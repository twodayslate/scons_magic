## SCons Magic

#### Build `program` (default)
```
scons
```

#### Build `program`
```
scons program
```

#### Build multiple versions of `program`
```
scons program program+platform@linux program+option@value
```

When `platform@linux` is set the program will act differently - same with `option@value`! Try it out/experiment with different options.

The `program`s will be exported to `export/`. All build files should be contained inside `build/`

Huge thanks to [bdbaddog](https://github.com/bdbaddog) for the guidance and support.
