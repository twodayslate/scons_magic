## SCons Magic

#### Build all `program`s (default)
```
scons
```

This build all variants of `program`

#### Build `program`
```
scons ???
```

This will build one variant of `program` with the host options

#### Build multiple versions of `program`
```
scons program_darwin_x86_64_64 program_linux_arm_64
```

This will build different variants of `program`

platform, arch, and bits are supported options. 

The `program`s will be exported to `export/`. All build files should be contained inside `build/`

Huge thanks to [bdbaddog](https://github.com/bdbaddog) for the guidance and support.
