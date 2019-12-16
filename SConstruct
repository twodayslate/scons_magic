import os


for target in COMMAND_LINE_TARGETS:
	self = PARSE_TARGET(target)
	Default(SConscript(dirs=['program'], variant_dir=os.path.join(GetLaunchDir(), target), exports=['self']))

if not COMMAND_LINE_TARGETS:
	self = PARSE_TARGET('program')
	Default(SConscript(dirs=['program'], variant_dir='build/program', exports=['self']))