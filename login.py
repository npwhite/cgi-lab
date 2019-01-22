#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()
import os
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

#print()

# if os.environ.has_key("HTTP_COOKIE"):
#     for cookie in map(strip, split(environ["HTTP_COOKIE"], ":")):
#         (key, value) = split(cookie, '=')
#         if key == "username":
#             c_username = value
#
#         if key == "password":
#             c_password = value

cookie_string = os.environ.get("HTTP_COOKIE")
cookie_pairs = cookie_string.split(":")
for pair in cookie_pairs:
    key, value = pair.split("=")
    if "username" in key:
        c_username = val
    elif "password" in key:
        c_password = val
c_username = ""
c_password = ""

if c_username == username and c_password==password:
    print("\n\n")

print("Content-Type: text/html")



if os.environ.get("REQUEST_METHOD", "GET") == "POST":
    form = cgi.FieldStorage()
    f_username = form.getvalue("username")
    f_password = form.getvalue("password")

    if f_username == username and f_password == password:
        print(username)
        print("Set-Cookie: username={}".format(username))
        print("Set-Cookie: username={}".format(password))
        print(secret_page(username, password))
        print("\n\n")

    else:
        print("\n\n")
        print(after_login_incorrect())

# print(os.environ)


# print("<h2>{}</h2>".format(username))
# print("<h3>{}</h3>".format(password))

else:
    print("\n\n")
    print(login_page())
