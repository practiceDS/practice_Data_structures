/* Swap all odds and even bits */
/* Given an unsigned integer, swap all odd bits with even bits. For example, if the given number is 23 (00010111), it should be converted to 43 (00101011). Every even position bit is swapped with adjacent bit on right side (even position bits are highlighted in binary representation of 23), and every odd position bit is swapped with adjacent on left side. */

#include<stdio.h>

int main()
{

	int x = 23;

	int even_bits, odd_bits, swap_bits;

	even_bits = (x & 0xAA) >> 1;
	odd_bits =  (x & 0x55) << 1;

	swap_bits = even_bits | odd_bits;

	printf("Number after swapping bits %d\n",swap_bits);

}
