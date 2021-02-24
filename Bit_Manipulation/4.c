/*  Binary representation of a given number using recursive approach */

#include <stdio.h>

int bin(unsigned int num)
{
	if(num > 0)
		bin(num/2);

	printf("%d",num % 2);

}



int main()
{

	bin(7);
	printf("\n");
	bin(4);

}
