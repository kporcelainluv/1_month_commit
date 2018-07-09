import requests

with open("1.txt") as fp:
    link = fp.readline().strip()
print(len(requests.get(link).text.splitlines()))
