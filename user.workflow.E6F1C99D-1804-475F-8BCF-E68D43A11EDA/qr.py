#coding:utf-8

import sys

from feedback import Feedback
import requests
import sys
import urllib
import re

fb = Feedback()
if len(sys.argv) >=2:
    query = sys.argv[1]
else:
    query = "{query}"

def gen_url(qr_query):
    return "http://qr.liantu.com/api.php?text={0}".format(urllib.quote_plus(qr_query))

def main():

    global query
    urls_list = []
    urls_list.append(query)
    if not query.startswith("http://"):
        urls_list.append("http://{0}".format(query))

    for url in urls_list:
        arg = gen_url(url)
        fb.add_item(title=url,arg=arg)
    print fb


if __name__ == '__main__':
    main()