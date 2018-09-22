import urllib
import urllib.request
import datetime
import re
import os.path

urls = ["https://www.pornhub.com/view_video.php?viewkey=ph5ae473c4c25f9", ]
urls = []
a = input("url here")
urls.append(a)
c = "1"
m = 1
while m:
    c = input("Enter to continue or input 'a' to add another video")

    if c == "":
        m = 0
    elif c == "a":
        m = 1
        a = input("url here")
        urls.append(a)
    else:
        print("Wrong command")

urls = set(urls)
print(len(urls), "video(s) to download...")
print(urls)
count = 0

for url in urls:
    count += 1
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \
- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("preparing to download", count, "of", len(urls))
    find_position = "a"
    the_url = "a"
    q = 1
    print('resolving')
    req = urllib.request.Request(url)
    print("requested")
    try:
        content = urllib.request.urlopen(req).read()
        print("content got")
    except urllib.error.URLError as e:
        print("\n", e, "\ninternet not available")


