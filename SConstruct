import os

for target in COMMAND_LINE_TARGETS:
	PARSE_TARGET(target).SConscript()

# Set the default behavior
if not COMMAND_LINE_TARGETS:
	Default(PARSE_TARGET('program').SConscript())
