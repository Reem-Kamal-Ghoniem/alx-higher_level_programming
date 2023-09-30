#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    content_b = response.read()
    content_S = content_b.decode('utf-8')
    print("Body response:")
    print(f"    - type: {type(content_bytes)}")
    print(f"    - content: {content_bytes}")
    print(f"    - utf8 content: {content_utf8}")
