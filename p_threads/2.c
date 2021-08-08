/*Threads :- Mutiple strands of execution in a program are threads */

/* This programs shows the threads execution without any synchrnization mechanism */

#include<stdio.h>
#include<pthread.h>
#include<string.h>

/* Declaring thread*/
pthread_t a_thread[5];

void *thread_func(void *arg)
{

	static int a = 1;
	printf("Thread %d started\n",a);
	printf("Thread %d finished\n",a);
	a = a + 1;
	return NULL;
}
int main()
{

	int i = 0;
	while (i <5)
	{
		if(pthread_create(&a_thread[i],NULL,&thread_func,NULL) != 0)
		{
			printf("thread creation failed\n");
			return;
		}

		i = i + 1;

	}
	
	pthread_join(a_thread[0],NULL);
	pthread_join(a_thread[1],NULL);
	pthread_join(a_thread[2],NULL);
	pthread_join(a_thread[3],NULL);
	pthread_join(a_thread[4],NULL);
}
