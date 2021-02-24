/*  Binary representation of a given number. */

#include <stdio.h>

int bin(unsigned int num)
{

	unsigned int i;

	for(i = 1 << 31 ; i > 0 ; i = i / 2)
		(num & i) ? printf("1"): printf("0");
}



int main()
{

	bin(7);
	printf("\n");
	bin(4);

}
