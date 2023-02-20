d="10.169.23.15"
h=f"GET /index.html HTTP/1.1\r\nHost: {d}\r\n\r\n"
x=(h).find("Host:")
print(h[(h).find("Host:")+6:(h).find("\r\n\r")])
print(1)