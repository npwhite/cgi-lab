#!/usr/bin/env python

# TODO:

import cgi
import cgitb
cgitb.enable()
import os
import json

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("/head")
print("<h2>Hello World</h2>")

# print query params
print("<dl>")
print("<dt>QUERY_STRING</dt>")
print("<dd>")
print(os.environ.get("QUERY_STRING"))
print("</dd>")
print("<dt>HTTP_USER_AGENT:</dt>")
HTTP_USER_AGENT = os.environ.get("HTTP_USER_AGENT", None)
#print(f"<dd>{os.environ.get("HTTP_USER_AGENT")}")
print("<dd>{}</dd>".format(HTTP_USER_AGENT))
print("</dl>")

print("<pre>")

env_json = {}
for key, value in os.environ.items():
    env_json[key] = value

print(json.dumps(env_json))

print("</prev>")
