#!/usr/bin/env python
	old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR ) 
	print "New sock state: %s" %new_state
	srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	srv.listen(1)