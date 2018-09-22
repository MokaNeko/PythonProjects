
import urllib.request

HEADERS = {'user-agent': 'Chrome/45.0.2454.101 Safari/537.36',
           'referer': 'http://www.pornhub.com/'}

#url = "https://www.baidu.com"
url = "https://www.pornhub.com/view_video.php?viewkey=ph5b45351ec6b19"
req = urllib.request.Request(url, headers=HEADERS)
print(req)
content = urllib.request.urlopen(req).read()

content = content.decode()

title_begin = content.find("<title>")
title_end = content.find("</title>")
title = content[title_begin+7:title_end]

print("title:", title)

print("title.decode:", title)

