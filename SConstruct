import os


for target in COMMAND_LINE_TARGETS:
	self = PARSE_TARGET(target)
	path = os.path.join('#/build', self.path())
	Default(SConscript(dirs=['program'], variant_dir=path, exports=['self']))

if not COMMAND_LINE_TARGETS:
	self = PARSE_TARGET('program')
	path = os.path.join('#/build', self.path())
	Default(SConscript(dirs=['program'], variant_dir=path, exports=['self']))