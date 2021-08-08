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
	char *hello = "Hello from the client";
	
	socket_fd = socket(AF_INET,SOCK_STREAM,0);
	if(socket_fd < 0)
	{
		perror("Socket creation failed\n");
	}

	address.sin_family = AF_INET;
	address.sin_addr.s_addr = inet_addr("127.0.0.1");
	address.sin_port = htons(PORT); 
	int address_len = sizeof(address);

	if(connect(socket_fd,(struct sockaddr *)&address,address_len) < 0)
	{
		perror("Connection refused\n");
	}	
	printf("Hello message sent to the server\n");	
	send(socket_fd,hello,strlen(hello),0);
	val_read = read(socket_fd,arr,1024);
	printf("Data recieved from server :-  %s\n",arr);
	
	close(socket_fd);
		


}

