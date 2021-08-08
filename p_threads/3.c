/*Threads :- Mutiple strands of execution in a program are threads,
Mutex : - It is uesd for the synchronization between two or more threads,it is a locking mechanism */

/* This programs shows the how to threads are synchronized using mutex	*/

#include<stdio.h>
#include<pthread.h>
#include<string.h>

/* Declaring thread*/
pthread_t a_thread[5];

/* Declaring Mutex*/
pthread_mutex_t lock;


void *thread_func(void *arg)
{

	pthread_mutex_lock(&lock);
	static int a = 1;
	printf("Thread %d started\n",a);
	printf("Thread %d finished\n",a);
	a = a + 1;
	pthread_mutex_unlock(&lock);
	return NULL;
}
int main()
{

	if(pthread_mutex_init(&lock,NULL) != 0)
	{
		printf("mutex initialization failed\n");
	}	
	
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
	pthread_mutex_destroy(&lock);
	
}
