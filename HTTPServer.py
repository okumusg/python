'This is a simple http server'

#!/usr/bin/python

import SimpleHTTPServer
import SocketServer

port = 10000 # Server port 

handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("",port),handler) # Creating a TCP Server

print "Http Server serving at ", port

httpd.serve_forever()