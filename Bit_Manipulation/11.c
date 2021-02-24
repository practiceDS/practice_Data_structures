/*  WAP to check whether a system is little endian or big endian. */

#include<stdio.h>

int main()

{
	unsigned int a = 1;
	char *ch = (char *)&a;

	if(*ch)
		printf("little Endian\n");
	else
		printf("Big Endian\n");



}
