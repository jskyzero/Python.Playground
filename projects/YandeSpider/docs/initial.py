"""Spider1.py
download post first page picture from yande.re
"""
import re
import os
import urllib2

# no use but waste my half day time
# import requests.packages.urllib3.util.ssl_
# print(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

if not os.path.exists('post'):
    os.mkdir('post')
os.chdir('post')

POST_PATTEN = re.compile(r'(?<=<span class="plid">#pl )https://yande.re/post/show/\d+(?=</span>)')
PAGE_PATTEN = re.compile(r'(?<=src\=")https://files.yande.re/\w+/\w+/yande\.re.+?\.\w+(?=")')
NAME_PATTEN = re.compile(r'(?<=/)\w{6,}')

RESPONSE = urllib2.urlopen("https://yande.re/post")
HTML = RESPONSE.read()
RESULT = re.findall(POST_PATTEN, HTML)

NUM = 0
for STR in  RESULT:
    FILE_NAME = re.findall(NAME_PATTEN, STR)[0]
    SHOW_RESPONSE = urllib2.urlopen(STR)
    SHOW_HTML = SHOW_RESPONSE.read()

    PIC_URL = re.findall(PAGE_PATTEN, SHOW_HTML)[0]
    PIC_REQUEST = urllib2.Request(PIC_URL)
    PIC_REQUEST.add_header("User-Agent", "Mozilla/5.0 (Macintosh; \
    Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/47.0.2526.106 Safari/537.36")
    PIC_RESPINSE = urllib2.urlopen(PIC_REQUEST)
    DATA = PIC_RESPINSE.read()

    FILE = open(FILE_NAME + ".jpg", 'w+')
    FILE.write(DATA)
    FILE.close()
    print NUM, FILE_NAME, "finished"
    NUM = NUM + 1


