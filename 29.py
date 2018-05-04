#爬虫
import urllib.request as url
#response = url.urlopen("http://www.fishc.com")

url1 = "http://www.fishc.com"
req = url.Request(url1)
response = url.urlopen(req)
html = response.read()
html = html.decode('utf-8')
print(html)





