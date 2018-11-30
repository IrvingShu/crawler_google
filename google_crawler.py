# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:45:53 2017

@author: za-chendan
"""
import os
import re
import urllib
import json
import socket
import requests
import urllib.request
import urllib.parse
import urllib.error
import time
from icrawler.builtin import GoogleImageCrawler

start=time.clock()
# dish names were stored in names_name 

names_name ='name.txt'
names_start = 1
names=[]
for line in open(names_name,encoding='UTF-8'):
    names.append(line.strip())
names=[x for x in names if x!='\ufeff']
#names = [line.strip() for line in open(names_name)]
 
dict_c2n = dict(zip(names, range(names_start, names_start+len(names))))
dict_n2c = dict(zip(range(names_start, names_start+len(names)), names))

for dishname in names:
    folder_name = str(dict_c2n[dishname])
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir':'/Users/irving/qyc/code/gluon/crawler_google/images/google/'+folder_name})

#picture——number is limited to 100
    google_crawler.crawl(keyword=dishname, max_num=500,
                             date_min=None, date_max=None,
                             min_size=(100,100), max_size=None)
end=time.clock()
# 打印运行时间
print(end-start)



