#!/usr/bin/env python3

import cgi
print("Content-type: text/html")
print()
our_form = cgi.FieldStorage();
in_name = our_form.getfirst("in_name", "не задано")
in_comment = our_form.getfirst("in_comment", "не задано")

print(in_name)
 
