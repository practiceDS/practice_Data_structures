#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#define PORT 8080

int main()
{
	int socket_fd;
	int new_sock_fd,val_read;
	char arr[1024];
	struct sockaddr_in address;
	char *hello = "Hello from the server";

	/* Used for creation of the socket */	
	socket_fd = socket(AF_INET,SOCK_STREAM,0);
	if(socket_fd < 0)
	{
		perror("Socket creation failed\n");
	}

	address.sin_family = AF_INET;
	address.sin_addr.s_addr = inet_addr("127.0.0.1");
	address.sin_port = htons(PORT); 
	int address_len = sizeof(address);
	/*Bind :- It is used to attach the created socket to a ip and a port */
	if(bind(socket_fd,(struct sockaddr *)&address,address_len) < 0)
	{
		perror("bind failed\n");
	}

	if(listen(socket_fd,3) < 0)
	{
		perror("listen failed\n");
	}
	
	new_sock_fd = accept(socket_fd,(struct sockaddr *)&address,&address_len);
	if(new_sock_fd < 0 )
	{
		perror("accept failed\n");
	}
	
	val_read = read(new_sock_fd,arr,1024);
	printf("Data recieved from client :-  %s\n",arr);
	send(new_sock_fd,hello,strlen(hello),0);
	printf("Hello message sent to the client\n");	
		
	close(socket_fd);
		


}

