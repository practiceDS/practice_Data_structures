/*Threads :- Mutiple strands of execution in a program are threads */
#include<stdio.h>
#include<pthread.h>
#include<string.h>

char message[] ="Hello World";

void *thread_func(void *arg)
{
	printf("thread start execution with arguments %s\n",(char *)arg);
	strcpy(message,"Bye");
	pthread_exit("Thread terminates");


}
int main()
{
	pthread_t a_thread;
	void *retval;
	if(pthread_create(&a_thread,NULL,&thread_func,(void *)message) != 0)
	{
		printf("thread creation failed\n");
		return;
	}
	
	printf("waiting for the thread to execute\n");
	
	if(pthread_join(a_thread,&retval) != 0)
	{
		printf("thread join failed\n");
		return;
	} 
	
	printf("The return value of thread is %s\n",(char*)retval);
	printf("The message after thread execution is %s\n",message); 

}
