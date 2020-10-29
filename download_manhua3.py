
from pprint import pprint
import urllib3
import re
import os
import json
import download_rule
from js_get_image_uri import duoduo_get_image_url


class DownloadManhua():
    def __init__(self, rule: download_rule.DuoDuoManHua):
        self._base_dir = None

        self._rule = rule
        self.http = urllib3.PoolManager()

        self._catalog_info = []
        self._catalog_url = None

    def base_dir(self, base_dir):
        self._base_dir = base_dir

    def get_url_resp(self, url):
        resp = self.http.request('GET', url)
        if resp.status != 200:
            print("Status code not 200")
            return

        return resp.data.decode('utf-8')

    def catalog_url(self, catalog_url):
        """
        分析目录页面
        """
        self._catalog_url = catalog_url

        # resp = self.http.request('GET', self._catalog_url)
        # if resp.status != 200:
        #     print("Status code not 200")
        #     return

        # resp_data = resp.data.decode('utf-8')
        resp_data = self.get_url_resp(self._catalog_url)

        self._get_catalog_info(resp_data)

    base_dir = property(fset=base_dir)
    catalog_url = property(fset=catalog_url)

    def _get_catalog_info(self, resp_data: str):
        search = re.search(self._rule.SEARCH_CATALOG, resp_data, re.DOTALL)
        if not search:
            print("Can't search any <chapter-warp> tag, Exit...")
            exit()

        all_li = search.group(1)

        titles = re.findall(self._rule.FIND_ALL_LI, all_li, re.DOTALL)

        info = []
        idx = 1
        for t in titles:
            li = re.search(self._rule.SEARCH_HERF_AND_TITLE, t, re.DOTALL)
            if self._catalog_url not in li.group(1):
                continue
            info.append({'index': str(idx).zfill(
                3), 'title': li.group(2), 'url': li.group(1)})
            idx += 1

        self._catalog_info = info
        return

    def get_base_message(self, url):
        """
        获取本章的基本信息
        """
        resp = self.http.request('GET', url)
        if resp.status != 200:
            print("Status code not 200")
            return

        resp_data = resp.data.decode('utf-8')

        info = {}
        info['title'] = self.get_title(resp_data)
        # info['chapter_image_url'] = self.get_chapter_path(resp_data)
        info['chapter_info'] = self.get_chapter_info(resp_data)
        info['next_chapter_url'] = self.get_next_chapter_url(resp_data)
        return info

    def get_title(self, resp_data: str):
        title = re.search(self._rule.SEARCH_TITLE, resp_data)
        if not title:
            print("can't found title, Exit...")
            exit()

        title = title.group(1)
        idx = len(title)
        i = title.find(self._rule.FIND_TITLE)
        if i:
            idx = i

        return title[0:idx]

    def get_next_chapter_url(self, resp_data: str):
        search_next_chapter_url = re.search(
            self._rule.SEARCH_NEXT_URL, resp_data, re.M | re.I)

        if not search_next_chapter_url:
            print("can't found next chapter url, Exit...")
            exit()

        return search_next_chapter_url.group(1).replace('\\', '')

    def get_page_length(self, resp_data):
        res = re.search(self._rule.SEARCH_IMAGE_PATH,
                        resp_data, re.M | re.I).group(1)
        return len(res.split(','))

    def get_page_image_url(self, url):
        """
        通过页面的JS代码还原出图像地址
        """
        resp_data = self.get_url_resp(url)
        res = re.search(self._rule.SEARCH_IMAGE_PAGE_JSCODE,
                        resp_data).group(1)

        res = duoduo_get_image_url(res)
        print(res)


if __name__ == '__main__':
    manhua = DownloadManhua(download_rule.DuoDuoManHua)
    # manhua.catalog_url = 'https://m.duoduomh.com/manhua/xuanfengguanjia'
    manhua.catalog_url = 'https://m.duoduomh.com/manhua/zhoushuhuizhan'

    manhua.base_dir = 'D:\图片\咒术回战'
    # pprint(manhua._catalog_info)

    for cata_dict in manhua._catalog_info:
        url = cata_dict['url']
        resp_data = manhua.get_url_resp(url)
        length = manhua.get_page_length(resp_data)
        cata_dict['image_urls'] = {}

        for idx in range(length):
            i = idx + 1
            page_url = re.sub('.html', '-'+str(i)+'.html', url)
            image_url = manhua.get_page_image_url(page_url)
            cata_dict['image_urls'][i] = image_url
            # print(image_url)

    json_str = json.dumps(manhua._catalog_info, indent=4)
    with open('manhua_download.json', 'w') as json_file:
        json_file.write(json_str)

    # test_url = 'https://m.duoduomh.com/manhua/zhoushuhuizhan/1058209-20.html'
    # manhua.get_page_image_url(test_url)
