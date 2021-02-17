/* Implement strupr function */
#include<stdio.h>

char strupr(char *p)
{
	while( *p != '\0')
	{
		if(*p >= 97 && *p <= 122 )
			*p = *p - 32;

		p++;

	}
	*p = '\0';

}

int main()
{
	char arr[]= "kushagrz";
	printf("Input:- %s\n",arr);
	strupr(arr);
	printf("Output:- %s\n",arr);

}
