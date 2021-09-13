#include<stdio.h>
#include<stdlib.h>

int main()
{

	int r = 2, c = 2;
	int i,j;
	int *arr[r];
	for (i = 0 ; i < r ; i++)
	{
		arr[i] = (int *)malloc(c * sizeof(int));
	}
	
	int count = 0;
	
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			arr[i][j] = ++count;
		}
	}


	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("%d",arr[i][j]);
		}
	}

	for(i=0;i<r;i++)
		free(arr[i]);

	free(arr);

}

