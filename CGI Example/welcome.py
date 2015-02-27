#!/usr/bin/python

import cgi, cgitb

#Creating instance of FieldStorage
form = cgi.FieldStorage()

#Getting value from keyname
firstName = form.getvalue('firstName')
lastName = form.getvalue('lastName')



print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Welcome</title>'
print '</head>'
print '<body>'
print '<h2>Welcome! %s %s</h2>' % (firstName,lastName)
print '</body>'
print '</html>'