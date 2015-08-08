#coding:utf-8

import sys

from feedback import Feedback
import requests
import sys

def check_is_ip_format(ip):
    _n = ip.split('.')
    if len(_n) != 4:
        return False
    for i in _n:
        try:
            int(i)
        except:
            return False
    return True

fb = Feedback()
if len(sys.argv) >=2:
    query = sys.argv[1]
else:
    query = "{query}"

if check_is_ip_format(query):
    valid = 'YES'
    url = "http://freeapi.ipip.net/{0}".format(query)
    r = requests.get(url).json()
    title = ''
    for _t in r[:3]:
        if _t not in title:
            title += _t
    subtitle = ''.join(r[3:])
    arg = title
else:
    valid = 'NO'
    title = query
    subtitle = ''
    arg = ''

fb.add_item(title, subtitle, valid=valid, arg=arg)
print fb