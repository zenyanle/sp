import requests as req
#import bs4
#from pprint import pprint
import re
import random
import threading as thrd
import time

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

def url_get(content):
    findlink3 = re.compile(r'data-src="(.*?)"')
    link3 = re.findall(findlink3, content)

    i = 0
    for name in link3:
        i += 1
        img_url = 'https://imeizi.me' + name
        img = req.get(img_url,headers=headers)
    #    f = open(f'{str(i)}.jpg','wb')
    #    f.write(img.content)
    #    f.close()

        try:
            with open(f'{many}_{i}.jpg', 'xb') as file:
                file.write(img.content)
        except Exception:
            break
        print(f'线程1正在下载{many}_{i}')

def url_get1(content):
    findlink3 = re.compile(r'data-src="(.*?)"')
    link3 = re.findall(findlink3, content)

    i = len(link3) + 1
    #for name in link3:
    for h in range(len(link3)-1,-1,-1):
        i = i-1
        name = link3[h]
        img_url = 'https://imeizi.me' + name
        img = req.get(img_url,headers=headers)
    #    f = open(f'{str(i)}.jpg','wb')
    #    f.write(img.content)
    #    f.close()

        try:
            with open(f'{many}_{i}.jpg', 'xb') as file:
                file.write(img.content)
        except Exception:
            break
        print(f'线程2正在下载{many}_{i}')


def stt():
    res = req.get(f'https://imeizi.me/article/{many}/',headers=headers)
    try:
        res.raise_for_status()
        #print(f'将要下载的图片编号为{many}')
        url_get(res.text)
    except Exception:
        print('404')

def stt1():
    res = req.get(f'https://imeizi.me/article/{many}/',headers=headers)
    try:
        res.raise_for_status()
        #print(f'将要下载的图片编号为{many}')
        url_get1(res.text)
    except Exception:
        print('404')


#start()

many = str(input('输入要爬的编号'))

dlthead = thrd.Thread(target=stt)
dlthead.start()

#time.sleep(1)

dlthead1 = thrd.Thread(target=stt1)
dlthead1.start()
print('开始')
