# -*- coding: UTF-8 -*-

from pprint import pprint
import urllib3
import re
import os
import download_rule


class DownloadManhua():
    def __init__(self, rule: download_rule.DuoDuoManHua):
        self._base_dir = None

        self._rule = rule
        self.http = urllib3.PoolManager()

        self._catalog_info = []
        self._catalog_url = None

    def base_dir(self, base_dir):
        self._base_dir = base_dir

    def catalog_url(self, catalog_url):
        self._catalog_url = catalog_url

        resp = self.http.request('GET', self._catalog_url)
        if resp.status != 200:
            print("Status code not 200")
            return

        resp_data = resp.data.decode('utf-8')

        self.get_catalog_info(resp_data)

    base_dir = property(fset=base_dir)
    catalog_url = property(fset=catalog_url)

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
        info['chapter_image_url'] = self.get_chapter_path(resp_data)
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

    def get_chapter_path(self, resp_data: str):
        search_image_res = re.search(
            self._rule.SEARCH_IMAGE_RES, resp_data, re.M | re.I)
        search_image_path = re.search(
            self._rule.SEARCH_IMAGE_PATH, resp_data, re.M | re.I)

        if not search_image_res or not search_image_path:
            print("can't found image path or image res, Exit...")
            exit()

        image_res: str = search_image_res.group(1)
        path: str = search_image_path.group(1)
        image_path_list: list = path[2:-1].split(",")

        index = 0
        for e in image_path_list:
            e = e.replace('"', '')
            e = e.replace('\\', '')
            image_path_list[index] = image_res + e
            index += 1

        return image_path_list

    def get_next_chapter_url(self, resp_data: str):
        search_next_chapter_url = re.search(
            self._rule.SEARCH_NEXT_URL, resp_data, re.M | re.I)

        if not search_next_chapter_url:
            print("can't found next chapter url, Exit...")
            exit()

        return search_next_chapter_url.group(1).replace('\\', '')

    def get_catalog_info(self, resp_data: str):
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

    def download(self):
        for info in self._catalog_info:
            chapter_info = self.get_base_message(info['url'])
            self.download_chapter_images(info, chapter_info)

    def download_chapter_images(self, info: dict, chapter_info: dict):
        chapter_dir = os.path.join(
            self._base_dir, info['index'] + "_" + info['title'])
        if not os.path.exists(chapter_dir):
            os.mkdir(chapter_dir)

        for url in chapter_info['chapter_image_url']:
            #file_name = self._info['chapter_num'] + '_' + url.split('/')[-1].replace('webp', 'jpg').zfill(6)
            file_name = url.split('/')[-1].replace('webp', 'jpg').zfill(6)
            full_file_path = os.path.join(chapter_dir, file_name)
            if os.path.isfile(full_file_path):
                print('Has image file, Skip - ', file_name)
                continue

            resp = self.http.request('GET', url)
            if resp.status != 200:
                print("Fail to Download ", url)
                continue

            with open(full_file_path, 'wb+') as f:
                f.write(resp.data)
                print('Success Download - ', file_name)


if __name__ == '__main__':
    manhua = DownloadManhua(download_rule.DuoDuoManHua)
    # manhua.catalog_url = 'https://m.duoduomh.com/manhua/xuanfengguanjia'
    manhua.catalog_url = 'https://m.zuimh.com/manhua/zhoushuhuizhan'

    manhua.base_dir = 'D:\图片\咒术回战'
    pprint(manhua._info)

    # manhua.download()
