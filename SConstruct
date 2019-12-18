for platform in ['darwin', 'linux']:
	for arch in ['i386','x86_64','arm']:
		for bits in ['32','64']:
			target = Target('program', platform, arch, bits)
			env = SpecialEnvironment() # setup environment addmethod
			env = Environment(TARGET_PLATFORM=platform, TARGET_ARCH=arch, TARGET_BITS=bits, VARIANT_DIR=target.variant_dir(),
                              EXPORT_DIR=target.export_dir(), LIBPATH=['$EXPORT_DIR'])
			SConscript('src/SConscript', variant_dir=target.variant_dir(), exports={'self': target, 'env': env})

