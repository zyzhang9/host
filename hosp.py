#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from urllib import request
from bs4 import  BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#req = request.Request('http://www.bjguahao.gov.cn/dpt/appoint/120-200000930.htm?week=0&relType=0&sdFirstId=0&sdSecondId=0', 
req = request.Request('http://www.bjgurhao.gov.cn', 
      headers={     'Host': 'www.bjguahao.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
})
res = request.urlopen(req)
# soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
 
print('all links')
links = soup.find_all('a')
 
for link in links:
    print(link.name, link['href'], link.get_text())

for link in links:
    print(link.name, link['href'], link.get_text())
    
print('all lacie links')
link_node = soup.find('a', href='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text()) 
 
print('re')
link_node = soup.find('a', href=re.compile(r"ill"))
print(link_node.name, link_node['href'], link_node.get_text())
 
print('all p text')
p_note = soup.find('p', class_="title")
print(p_note.name, p_note.get_text())

