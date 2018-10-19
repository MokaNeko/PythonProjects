import urllib.request
import urllib
import win32clipboard

Header = {
'Host':'do.ishadowx.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 \
Safari/537.36',
'Referer': 'https://www.pornhub.com/'}

version = "0.5"
print("-----------SSR Password Fetcher-----------\
\n"+'----------------- V'+version+" -----------------\n")

req = urllib.request.Request('https://do.ishadowx.com', headers=Header)
content = urllib.request.urlopen(req).read()
content = content.decode()

server_begin = content.find("jpb.isxa.top")
server_end = content.find("Japan-Linode2")
server = content[server_begin:server_end]

pwd = server.find("\"pwjpb\">")
pwd = server[pwd+8:pwd+23]

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(pwd)
win32clipboard.CloseClipboard()
print('password', pwd, 'has been copied to clipboard')

a = input('press \'Enter\' to exit')

#print(server)
#print(content)
