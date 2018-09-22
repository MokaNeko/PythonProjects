import urllib.request
import http.cookiejar
url = 'http://war.163.com/photoview/4T8E0001/2281894.html'
# 以字典形式设置headers，格式是[(字段名，字段值),(字段名，字段值)]，这里先用字典，在下面会用for把它转为列表元组的形式
h = {
	'Accept': 'text/html,application/xhtml+xml,application\
	/xml;q=0.9,image/webp,*/*;q=0.8',

	'Accept-Language': 'zh-CN,zh;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit\
	/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',

	'Connection': 'keep-alive',
	'referer': 'http://www.163.com/'}
# 设置cookie
cj = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler(
	{'http': '127.0.0.1:8888'})  # 这里设置代理服务器是为了方便Fiddler抓包，实际可以这里可以省去
op = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,
                                 urllib.request.HTTPCookieProcessor(
	                                 cj))  # 将代理服务器和headrest信息，作为一个对象赋给op

headall = []  # 建立空列表，构造出指定格式的headers信息
for key, value in h.items():  # 循环字典h，每次循环提取一个键值对
	item = (key, value)  # 把提取到的键值对，做成元组赋予item
	headall.append(item)  # 添加到列表中
op.addheaders = headall  # 将指定格式的headrest信息添加好
urllib.request.install_opener(op)  # 安装为全局，下面直接用urllib时就自动把op的对象加进去了
print(headall)
data = urllib.request.urlopen(url).read()
f = open('D:/AuI18N/5.html', 'wb')
f.write(data)
f.close()
