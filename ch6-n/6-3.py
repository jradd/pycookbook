#coding=utf-8
'6-3 Parsing Simple XML Data'

from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
u = urlopen('http://qdaily.com/feed.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title) # .decode('utf-8')
    print(date)
    print(link)
    # print()