#coding=utf-8
'6-3-1 Parsing Simple XML Data'

from urllib.request import urlopen
from xml.etree.ElementTree import parse
from datetime import datetime
# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
u = urlopen('http://qdaily.com/feed.xml')
doc = parse(u)

# Extract and output tags of interest

d = datetime.now()
with open('haoqixin.md','w') as f:
    f.write('好奇心日报\n')
    f.write('=============\n')
    f.write('refresh date:'+ str(d.isoformat()) + '\n')
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')
        print(title); title = title.strip()
        print(date);
        print(link); link = link.strip()
        f.write('## Title: [{}]({})\n'.format(title, link))
        print('\n')
        f.write('## Title-date:\t'+ date + '\n\n'); print()
        print('\n\n')