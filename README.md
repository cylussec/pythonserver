Protocol Mimicry -- Developer Homework

Please provide executable Python code for each question

1.) Develop a client and server using the Python socket library that operates as
follows.
- Client application is given a server IP address (in dotted decimal notation),
a port, and a password as command line parameters.
- Server is given a port to run on and a path to the password list included with
this assignment (in CSV format) as command line parameters.  The password list
maps a password to an integer, x.
- Client starts by creating a TCP connection to the server, sending the
password, and awaiting confirmation from the server.
- The server receives the passwords, looks up the associated integer x, and
sends confirmation to the client.
- Once the connection is established, the client application will read integers,
N, interactively from the user and send them to the server.  The server will
calculate N^x and return it to the client (resulting number could be quite
large).
- Client must gracefully close the connection when the application is terminated
(e.g., via SIGINT).

2.) Create unit tests for the client and server applications above.

3.) Extend the server to support multiple concurrent connections from different
clients (potentially with different passwords) using the multiprocessing
library.

BONUS:  Describe or show how you would improve the protocol above to make it
resilient to an active man-in-the-middle adversary who may attempt to alter the
data sent between the client and server.


Passwords:
password	 x
avogadro	6022
fibonacci	11235
einstein	6673
newton	    98
