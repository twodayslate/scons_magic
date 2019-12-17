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
scons ??? ??? ???
```

This will build three different variants of `program`

platform, arch, and bits are supported options. 

The `program`s will be exported to `export/`. All build files should be contained inside `build/`

Huge thanks to [bdbaddog](https://github.com/bdbaddog) for the guidance and support.
