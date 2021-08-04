import requests as req
#import bs4
#from pprint import pprint
import re
import random
import threading as thrd

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

def url_get(content,ranum):
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
            with open(f'{ranum}_{i}.jpg', 'wb') as file:
                file.write(img.content)
        except Exception:
            continue
        print(f'正在下载{ranum}_{i}')


def stt():
    while True:
        many = random.randint(1,9200)
        res = req.get(f'https://imeizi.me/article/{many}/',headers=headers)
        try:
            res.raise_for_status()
            print(f'将要下载的图片编号为{many}')
            url_get(res.text,many)
        except Exception:
            print('404')
            continue

#start()

math = int(input('输入线程数'))

for n in range(1,math + 1):
    dlthead = thrd.Thread(target=stt)
    dlthead.start()
    print(f'第{n}线程开始')
