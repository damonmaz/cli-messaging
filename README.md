##KNOWN BUGS TO FIX:

-When a client exits using keyboard interrupt, the server raises an error because of the server set keeping track of clients
  -Maybe send a custom message when client wants to quit
-"MSG:" does not stay at the bottom of the command prompt, and it looks weird
-Need better way of distinguishing between clients besides username (maybe use Colorama)
