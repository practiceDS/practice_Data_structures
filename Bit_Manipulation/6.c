/* Rotate bits of a given number by d times */

/* Rotation can be of 2 types left rotation and Right Rotation , for eg :- num = 229 has to be rotated left 3 times
 * Binary Rep of 229 is = (11100101) , its left rotaion will be (00101111).
 * Opposite is the case for right rotation, its right rotaion will be (10111100) */


#include<stdio.h>
#define INT_BITS	32


int rightRotate(unsigned int num,int d)
{

	unsigned int val;
	val = (num >> d) | (num << (INT_BITS - d));
	return val;

}

int leftRotate(unsigned int num,int d)
{

	unsigned int val;
	val = (num << d) | (num >> (INT_BITS - d));
	return val;

}

int main()
{
	unsigned int num = 16;
	unsigned int d = 2;
	unsigned int val;
	val = leftRotate(num,d);
	printf("\nLeft Rotated value is %d\n",val);
	val = rightRotate(num,d);
	printf("\nRight Rotated value is %d\n",val);


}
