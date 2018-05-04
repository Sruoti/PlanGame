import urllib.request
import re
import os

def url_open(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')
        response = urllib.request.urlopen(req)
        html = response.read()
        return html
    except urllib.error.HTTPError:
        return '404'

def get_img(url):
    html = url_open(url)
    if html == '404':
        print(404)
        return '404'
    html = html.decode('utf-8')

    reg = r'<img src="([^"]+\.jpg)'
    img_addrs = re.findall(reg, html)
    save_img(img_addrs)


def save_img(address,folder="OOXX3"):
    if os.path.exists(folder) == False:
        os.mkdir(folder)
    os.chdir(folder)

    img_addrs = address

    for each in img_addrs:
        filename = each.split('/')[-1]

        print(each)   #正则中使用组来包裹时，findall会返回这个组的值。所以each不用在切割

        urllib.request.urlretrieve(each,filename,None)

if __name__ == "__main__":
    url = "http://www.mzitu.com/129326/11a30-19"
    get_img(url)





