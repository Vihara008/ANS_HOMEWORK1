#include	"utils.h"		/* Header file */

void
str_cli(FILE *fp, int sockfd)
{
	int		maxfdp1;
	fd_set		rset;
	char		sendline[MAXLINE], recvline[MAXLINE];

	FD_ZERO(&rset);
	for ( ; ; ) 
    {
        //Replace x with the correct parameter values
		FD_SET(fileno(fp), x);
		FD_SET(x , &rset);
        
		maxfdp1 = max(fileno(fp), sockfd) + 1;
        // Complete the select() function
		Select();

        //Replace x with the correct file descriptor value
		if (FD_ISSET(x , &rset)) 
        {	/* socket is readable */
			if (Readline(sockfd, recvline, MAXLINE) == 0)
				err_quit("str_cli: server terminated prematurely");
			Fputs(recvline, stdout);
		}

		//Replace x with the correct file descriptor value
		if (FD_ISSET(x , &rset)) 
        {  /* input is readable */
			if (Fgets(sendline, MAXLINE, fp) == NULL)
				return;		/* all done */
			Writen(sockfd, sendline, strlen(sendline));
		}
	}
}