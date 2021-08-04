import requests as re
import json
import time
import threading as thrd

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

def get_img(m,h):
    while True:
        res = re.get('https://api.lolicon.app/setu/v2?proxy=api.pixiv.moe/image/i.pximg.net/', headers=headers)
        try:
            res.raise_for_status()
        except Exception:
            continue
        pdata = json.loads(res.text)

        geshi = pdata['data'][0]['ext']
        name = pdata['data'][0]['title']
        d = pdata['data'][0]['urls']['original']
        h += 1
        print(f'第{m}线程 第{h}次下载 地址：{d}')

        imgr = re.get(d, headers=headers)
        try:
            imgr.raise_for_status()
        except Exception:
            continue
        img = imgr.content

        try:
            with open(f'{name}.{geshi}', 'wb') as file:
                file.write(imgr.content)
        except Exception:
            continue

        #n += 1
        #print(f"正在开始第{n}次下载")

num = int(input('输入线程数（推荐3）'))

for n in range(1,num + 1):
    dlthead = thrd.Thread(target=get_img, args=(n,0))
    dlthead.start()
    print(f'第{n}线程开始')
