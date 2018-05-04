import urllib.request

url = 'http://www.sina.com'
#'http://www.whatismyip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http':'115.223.230.191:9000'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')]
#response = urllib.request.install_opener(opener)
response = opener.open(url)
html = response.read().decode('utf-8')
print(html)
