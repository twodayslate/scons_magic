# if COMMAND_LINE_TARGETS:
# 	Default(SConscript(dirs=COMMAND_LINE_TARGETS))
# else:
# 	Default(SConscript(dirs=['program']))

CustomInit()

if not MY_CUSTOM_TARGETS:
	MY_CUSTOM_TARGETS.append(Target('program'))

print(MY_CUSTOM_TARGETS)

for target in MY_CUSTOM_TARGETS:
	print("Setting '%s' SConscript" % target.name)
	BUILD_TARGETS.append(target.name)
	Default(target.SConscript())