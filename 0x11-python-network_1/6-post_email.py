#!/usr/bin/python3
"""posting email address to a certain URL"""
import requests
import sys

if __name__ == "__main__":
    if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    responce = requests.post(url, data={'email': email})
    print(responce.text)
