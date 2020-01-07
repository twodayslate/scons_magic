#include <stdio.h>

int main() {
	char *hello = SCONS_OBFUSCATE("Hello world!");
	printf("%s\n",hello);
}