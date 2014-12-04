# -*- coding: utf-8 -*-
'6-3-1 Parsing Simple XML Data'

from urllib.request import urlopen
from xml.etree.ElementTree import parse
from datetime import datetime
import sys
print(sys.getdefaultencoding())
# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
u = urlopen('http://qdaily.com/feed.xml')
doc = parse(u)

# Extract and output tags of interest

d = datetime.now()
with open('haoqixin.md','w', encoding='utf-8') as f:
    f.write('Qdaily RSS Resource\n')
    f.write('=============\n')
    f.write('refresh date:'+ str(d.isoformat()) + '\n')
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')
        # print(title); print(date); print(link);
        title = title.strip() #.encode('utf-8')
        link = link.strip()   #.encode('utf-8')
        f.write('## Title: [{}]({})\n'.format(title, link))
        print('\n')
        f.write('## Title-date:\t'+ date + '\n\n'); print()
        print('\n\n')