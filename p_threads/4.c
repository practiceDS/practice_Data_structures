/*Threads :- Mutiple strands of execution in a program are threads,
Semaphore : - It is uesd for the synchronization between two or more threads,it is a signalling mechanism */

/* This programs shows the how to threads are synchronized using semaphores	*/

#include<stdio.h>
#include<pthread.h>
#include<string.h>
#include<semaphore.h>

/* Declaring thread*/
pthread_t a_thread[3];

/* Declaring semaphore*/
sem_t lock;


void *thread_func(void *arg)
{

	sem_wait(&lock);
	static int a = 1;
	printf("Thread %d started\n",a);
	printf("Thread %d finished\n",a);
	a = a + 1;
	sem_post(&lock);
	return NULL;
}
int main()
{

	if(sem_init(&lock,0,1) != 0)
	{
		printf("semaphore initialization failed\n");
	}	
	
	int i = 0;
	while (i <3)
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
	sem_destroy(&lock);
	
}
