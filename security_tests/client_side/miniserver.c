#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char** argv) {

  int lsock,csock,x;
  struct sockaddr_in saddr;
  
  if (argc-3) { 
    fprintf(stderr,"Usage: %s port handler_prog\n",argv[0]);
    exit(1); 
  }
  
  lsock=socket(AF_INET,SOCK_STREAM,0);
  
  x=sizeof(saddr);
  saddr.sin_family=AF_INET;
  saddr.sin_addr.s_addr=INADDR_ANY;
  saddr.sin_port=htons(atoi(argv[1]));
  
  if (bind(lsock,(struct sockaddr*)&saddr,x)) {
    perror("bind");
    exit(1);
  }
  
  listen(lsock,10);
  
  fprintf(stderr,"mini-server ready, %d/tcp -> %s...\n",atoi(argv[1]),argv[2]);
  
  while ((csock=accept(lsock,(struct sockaddr*)&saddr,(unsigned int*)&x)) >= 0) {
    int foo;
  
    fprintf(stderr,"Got a connection...\n");
    
    if (!fork()) {
      char buf[1024];
      
      read(csock,buf,sizeof(buf)); /* sink */

      dup2(csock,0);
      dup2(csock,1);
      close(csock);
      close(lsock);	
      execlp(argv[2],argv[2], 0);
      perror(argv[2]);
      exit(1);
    }
      
    close(csock);
    waitpid(-1,&foo,WNOHANG); /* sinkety sink */
      
  }
 
  return 0;

}
  
