import urllib.request
import urllib
import datetime
import re
import os.path

version = "1.4"
print("-----------PornHub Downloader-----------\
\n"+'----------------- V'+version+" -----------------\n")


def save_file(this_download_url, path, q):
    global E
    print("\nresolved,downloading\n")
    time1 = datetime.datetime.now()
    print(str(time1)[:-7],)
    if os.path.isfile(path):
        file_size = os.path.getsize(path)/1024/1024
        print("File "+path+" (" + str(file_size)+"Mb) already exists.")
        return
    else:
        print("Downloading\n\n"+path+"    "+q+"p\n\n\
this may take a long time which depends on your network quality")
        try:
            f = urllib.request.urlopen(this_download_url)
        except urllib.error.URLError as e:
            print("\n"+str(e)+"\n")
            E = 1
        else:
            data = f.read()
            with open(path, "wb") as code:
                code.write(data)
            time2 = datetime.datetime.now()
            print(str(time2)[:-7],)
            print(path+" Done.")
            use_time = time2-time1
            print("Time used: "+str(use_time)[:-7]+", ", )
            file_size = os.path.getsize(path)/1024/1024
            print("File size: "+str(file_size)+" MB, \
Speed: "+str(file_size/(use_time.total_seconds()))[:4]+"MB/s")


def download_the_av(url_d):
    global E
    Header['Referer'] = url_d
    print(Header['Referer'])
    find_position = "a"
    the_url = "a"
    q = 1
    print('resolving')
    try:
        req = urllib.request.Request(url_d, headers=Header)
    except ValueError as e:
        print("\n"+str(e)+"request not sent\n")
        E = 1
    else:
        print("requested,waiting for response")
        try:
            content = urllib.request.urlopen(req).read()
        except urllib.error.URLError as e:
            print("\n"+str(e)+"empty content got\n")
            E = 1
        else:
            print("content got")
            while len(content) < 100:
                print("try again...")
                content = urllib.request.urlopen(req).read()
            content = content.decode()
            title_begin = content.find("<title>")
            title_end = content.find("</title>")
            title = content[title_begin+7:title_end-14]
            title = title.replace('/', '_')
            title = filter(lambda x: x in " _-0123456789\
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", title)
            title = ''.join(list(title))
            quality = ['720', '480', '240']
            for i in quality:
                find_position = content.find(r'"quality":"'+i+'"')
                if find_position > 0:
                    q = i
                    break
            to_find = content[find_position:find_position+4000]
            pattern = re.compile(r"\"videoUrl\":\"[^\"]*\"")
            match = pattern.search(to_find)
            if match:
                the_url = match.group()
            the_url = the_url[12:-1]    # the real url
            the_url = the_url.replace(r"\/", "/")
            print(big_path)
            save_file(the_url, big_path + '\\download\\' + title + ".mp4", q)


E = 0
Header = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0)\
 Gecko/20100101 Firefox/61.0',
'Referer': 'https://www.pornhub.com/'}

big_path = os.getcwd()

urls = []
arg = input("input the link below:\n")
urls.append(arg)
while arg:
    arg = input("'Enter' to continue or type another link\n")
    print('input your path or use the default path: ', big_path)
    path2 = input()
    if path2 != "":
        big_path = path2
        print("your new path will be", big_path)
    if arg != "":
        urls.append(arg)
urls = set(urls)
print(len(urls), "video(s) to download...")
print('\n'.join(urls))
count = 0
for url in urls:
    count += 1
    print("- - - - - - - - - - - - - - - - - - - - -")
    print("preparing to download", count, "of", len(urls))
    download_the_av(url)
if E == 0:
    print("\nAll done")
else:
    print("Error Occurred")
