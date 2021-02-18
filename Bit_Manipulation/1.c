/* Count number of 1s in the binary representation of a number */
#include<stdio.h>

int main()
{

	int num = 7;
	int count = 0;
	int r;
	while(num)
	{
		r = num % 2;

		if(r == 1)
			count++;

		num = num/2;

	}

	printf("Number of 1s in binary rep is[%d]",count);

}
