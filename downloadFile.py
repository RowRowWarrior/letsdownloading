#!/usr/bin/env python3
import requests
res = requests.get(url)
print(res.text) # this only works for plain text
