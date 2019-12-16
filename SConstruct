# if COMMAND_LINE_TARGETS:
# 	Default(SConscript(dirs=COMMAND_LINE_TARGETS))
# else:
# 	Default(SConscript(dirs=['program']))

CustomInit()

print(MY_CUSTOM_TARGETS)

for target in MY_CUSTOM_TARGETS:
	print("Setting '%s' SConscript" % target.name)
	Default(target.SConscript())