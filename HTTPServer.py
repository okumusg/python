'This is a simple http server'

#!/usr/bin/python

import SimpleHTTPServer
import SocketServer

port = 10000 # Server port 

handler = SimpleHTTPServer.SimpleHTTPRequestHandler # Creating HTTP handler instance

httpd = SocketServer.TCPServer(("",port),handler) # Creating a TCP Server with HTTP handler

print "Http Server serving at ", port

httpd.serve_forever()
