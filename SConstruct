for plat in ['darwin', 'linux']:
	for arch in ['i386','x86_64','arm']:
		for bits in ['32','64']:
			target = Target('program', plat, arch, bits)
			env = Environment(TARGET_PLATFORM=target.platform, TARGET_ARCH=target.arch, TARGET_BITS=target.bits, VARIANT_DIR=target.variant_dir(),
                              EXPORT_DIR=target.export_dir(), LIBPATH=['$EXPORT_DIR'])
			SConscript('src/SConscript', variant_dir=target.variant_dir(), exports={'self': target, 'env': env})

