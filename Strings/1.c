/* Implement strlwr function */
#include<stdio.h>

char strlwr(char *p)
{
	while( *p != '\0')
	{
		if(*p >= 65 && *p <= 90 )
			*p = *p + 32;

		p++;

	}
	*p = '\0';

}

int main()
{
	char arr[]= "KUSHAGRA";
	printf("Input %s\n",arr);
	strlwr(arr);
	printf("Output %s\n",arr);

}
