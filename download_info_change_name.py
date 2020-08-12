import urllib3
import re
import os
from pprint import pprint


url = 'https://m.duoduomh.com/manhua/xuanfengguanjia'

http = urllib3.PoolManager()

resp = http.request('GET', url)

if resp.status != 200:
    print("Error Code, Exit...")
    exit()

data = resp.data.decode('utf-8')
search = re.search(r'<div class="chapter-warp">(.*?)</div>', data, re.DOTALL)
if not search:
    print("Can't search any <li> tag, Exit...")
    exit()

all_li = search.group(1)

titles = re.findall(r'<li>(.*?)</li>', all_li, re.DOTALL)
# pprint(titles[1])

# li = re.search(r'href="(.*?)".*<span>(.*?)</span>', titles[3], re.DOTALL)
# pprint(li.group(1))
# pprint(li.group(2))

info = []
idx = 1
for t in titles:
    li = re.search(r'href="(.*?)".*<span>(.*?)</span>', t, re.DOTALL)
    if url not in li.group(1): continue
    info.append({'index': str(idx).zfill(3), 'title': li.group(2), 'url': li.group(1)})
    idx += 1

# pprint(info)


# os.chdir('')
ldir = os.listdir(".")
pprint(ldir)

# for i in info:
#     src_name = "旋风管家" + i['title']
#     dst_name = i['index'] + "_" + i['title']
#     print(src_name, dst_name)
#     if src_name not in ldir: continue

#     os.rename(src_name, dst_name)

