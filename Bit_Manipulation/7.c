/* Count number of bits to be flipped to convert A to B */

#include<stdio.h>

int count_bits(int num)
{
	int count = 0;
	while(num)
	{
		count = count + (num & 1);
		num = num >> 1;


	}	
	return count;

}

int main()
{

	int A = 146;
	int B = 137;
	int num = A ^ B;
	int val = count_bits(num);
	printf("Number of bits to be flipped %d\n",val);

}
