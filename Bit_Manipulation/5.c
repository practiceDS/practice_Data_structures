/* Count number of 1s in the binary representation of a number using bitwise operator */
#include<stdio.h>

int main()
{

	int num = 7;
	static int count = 0;
	int r;
	while(num)
	{
		count = count + (num & 1);
		num = num >> 1;
	}

	printf("Number of 1s in binary rep is[%d]",count);

}
