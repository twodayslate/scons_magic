import os


for target in COMMAND_LINE_TARGETS:
	self = PARSE_TARGET(target)
	SConscript(dirs=[self.name], variant_dir=self.variantDir(), exports=['self'])

# Set the default behavior
if not COMMAND_LINE_TARGETS:
	self = PARSE_TARGET('program')
	Default(SConscript(dirs=[self.name], variant_dir=self.variantDir(), exports=['self']))