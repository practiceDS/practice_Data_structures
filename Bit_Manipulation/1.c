/* Count number of 1's in the binary representation of a number */

#include<stdio.h>

int main()
{

	int num = 7;
	int count = 0;
	while(num)
	{
		if(num % 2 != 0)
		{
			count++;
		}
		
		num = num >> 1;	

	}
	
	printf("The number of 1's is = %d\n",count);


}
