#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    t = r.text
    print("Body response:")
    print("\t- type: {}".format(type(t)))
    print("\t- content: {}".format(t))
