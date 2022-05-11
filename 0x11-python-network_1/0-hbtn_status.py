#!/usr/bin/python3
url = "https://intranet.hbtn.io/status"

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200

print(website_is_up)
