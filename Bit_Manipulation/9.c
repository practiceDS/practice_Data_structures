/* Find the element that appears once in an array where every other element appears twice */

#include<stdio.h>

int main()
{

	int arr[]= {7,3,5,4,5,3,4};
	int size = sizeof(arr)/sizeof(arr[0]);
	int i;
	int res = arr[0];
	for(i = 1 ; i < size ; i++)
	{
		res = res ^ arr[i];
		
	
	}

	printf("Element appears once is %d\n",res);

}

