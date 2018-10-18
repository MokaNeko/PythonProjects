urls = []
arg = input("input the link below:\n")
urls.append(arg)
while arg:
    arg = input("'Enter' to continue or type another link\n")
    urls.append(arg)

urls = set(urls)
print(len(urls), "video(s) to download...")
print('\n'.join(urls))
