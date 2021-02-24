/* Swap two nibbles in a byte. */
/* Eg:- number = 100, its binary rep is (0110 0100) , after swapping nibble it becomes ( 0100 0110) i.e - 70*/

#include<stdio.h>

int main()

{

	int num = 100;
	int val_1 = (num & 0x0F) << 4;
	int val_2 = (num & 0xF0) >> 4;

	int swap_num = val_1 | val_2;

	printf("Swapped number is %d\n",swap_num);
	

}
