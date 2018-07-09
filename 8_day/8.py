import os
import requests
url = "https://stepic.org/media/attachments/course67/3.6.3/"
first_url = os.path.join(url, "699991.txt")
while True:
    requests_open = (requests.get(first_url)).text
    print(requests_open)
    if "We" in requests_open:
        print(requests_open)
        break
    else:
        first_url = os.path.join(url, requests_open)


