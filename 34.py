import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page')+23
    b = html.find(']', a)
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    reg = r'<img src="[^"]+\.jpg'
    img_addrs = re.findall(reg,html)
    return img_addrs


def save_imgs(folder, img_address):
    for each in img_address:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder="00XX2", pages=10):

    if os.path.exists(folder) == False:
        os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))   #打开首页的当前页码

    testurl = 'http://jandan.net/ooxx/page-77#comments'

    for i in range(1):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'  #当前页的URL
        #img_addrs = find_imgs(page_url)    #当前页中的所有图片地址

        img_addrs = find_imgs(testurl)
        save_imgs(folder,img_addrs)      #保存图片


if __name__ == '__main__':
    download_mm()
