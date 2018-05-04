import urllib.request
import urllib.parse
import json

header = {}
header['User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

url = 'http://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh'
data = {'callback': 'jQuery32108942817301138704_1524559097656',
        'text': '我爱FISCH.COM',
        'ie': 'utf-8',
        'version': '0',
        'from': 'FanyiWeb',
        '_': '1524559097660'}
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data,header)

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

print(req.headers)
