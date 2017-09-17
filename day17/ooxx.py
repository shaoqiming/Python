# coding:utf-8

import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
    except:
        print("错误："+url)

def get_page(url):
    html= url_open(url).decode('utf-8')
    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    print(html[a:b])
    return html[a:b]


def find_image(url):
    html = url_open(url).decode('utf-8')
    img_address=[]
    a=0
    i=0
    while(a!=-1):
        a=html.find("img src=",i)
        b=html.find(".jpg",a,a+255)
        if b!=-1:
            print("11:",html[a+11:b+4])
            img_address.append(html[a+9:b+4])
            a = a + 9
        else:
            a=-1
        i=a

    return img_address;


def save_image(folder,image_addre):
    for image in image_addre:
        filenname=image.split('/')[-1]
        print("save：",image)
        with open(filenname, "wb") as f:
            img = url_open("http:"+image)
            f.write(img)





def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx'
    #获得页码
    page_num=int(get_page(url))

    for i in range(pages):
        page_num-=i
        page_url=url+'/page-'+str(page_num)+"#comments"
        #获得这页的图片地址
        img_addrs=find_image(page_url)
        #通过图片地址保存
        save_image(folder,img_addrs)

download_mm();