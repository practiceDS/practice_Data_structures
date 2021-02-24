/* Check whether a given number is even or odd without using any operator(+,-,*,%,/). */

#include<stdio.h>

int main()
{

	int num;
	printf("Enter number\n");
	scanf("%d",&num);
	int val = num & 1;
	if((val % 2) == 1)
		printf("ODD\n");
	else
		printf("EVEN\n");
}
