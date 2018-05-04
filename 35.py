import urllib.request
import os
import re


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


# 当这个页面需要有页码的时候
def get_page(url):
    pass


def find_imgs(url):
    html = url_open(url)
    if '404' == html:
        return '404'
    html = html.decode('utf-8')
    reg = r'src="http://[^"]+\.jpg'
    img_addrs = re.findall(reg, html)
    return img_addrs


def save_imgs(folder, img_address):
    for each in img_address:

        #图片url下载地址
        url = each.split('="')[1]

        #图片名
        filename = each.split('/')[-1]  # 这个-1有点6

        with open(filename, 'wb') as f:
            try:
                img = url_open(url)
                f.write(img)
            except urllib.error.HTTPError:
                print(url,"发生了错误")


def download_mm(folder="00XX", n=2000):
    if os.path.exists(folder) == False:
        os.mkdir(folder)
    os.chdir(folder)

    url = "http://www.cc900.cn/"
    # page_num = int(get_page(url))   #打开首页的当前页码
    page_num = 3000
    m = 50
    page_num += m       #i到50了 。下次设定m设定为50

    for i in range(n):
        page_num += 1
        page_url = url + str(page_num) + '.html'  # 当前页的URL
        print('当前i的值是%d'% i)
        #test_url = 'http://www.cc900.cn/3449.html'

        fing_imgs_result = find_imgs(page_url)

       # fing_imgs_result = find_imgs(test_url)
        if '404' == fing_imgs_result:
            continue

        img_addrs = fing_imgs_result  # 当前页中的所有图片地址
        save_imgs(folder, img_addrs)  # 保存图片


if __name__ == '__main__':
    download_mm()
