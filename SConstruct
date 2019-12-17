for platform in ['darwin', 'linux']:
	for arch in ['i386','x86_64','arm']:
		for bits in ['32','64']:
		    target = Target('program', platform, arch, bits)
		    SConscript(dirs=['program'], variant_dir=target.variant_dir(), exports={'self': target})
