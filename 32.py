import urllib.request
import os


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
    #print(html)
    img_addrs = []
    a = html.find('img src')

    while a != -1:
        b = html.find('.jpg',a)  #从a开始，最多到a+255处
        print('b:',b)
        if b != -1:
            img_addrs.append(html[a + 9:b + 4])
        else:
            b = a + 9
        a = html.find('img src=',b)  #下一次寻找，是为了寻找所有的图片
    return img_addrs

def save_imgs(folder, img_address):
    for each in img_address:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder="00XX", pages=10):

    if os.path.exists(folder) == False:
        os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))   #打开首页的当前页码

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'  #当前页的URL
        img_addrs = find_imgs(page_url)    #当前页中的所有图片地址
        save_imgs(folder,img_addrs)      #保存图片


if __name__ == '__main__':
    download_mm()
