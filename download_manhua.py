# -*- coding: UTF-8 -*-

from pprint import pprint
import urllib3
import re
import os
import download_rule

class DownloadManhua():
    def __init__(self, rule:download_rule.DuoDuoManHua):
        self._base_url = None
        self._base_dir = None
        self._rule = rule
        self.http = urllib3.PoolManager()
        self._info = {}


    def base_url(self, base_url):
        self._base_url = base_url

    def base_dir(self, base_dir):
        self._base_dir = base_dir
    
    base_url = property(fset=base_url)
    base_dir = property(fset=base_dir)

    def get_base_message(self):
        """
        获取本章的基本信息
        """
        resp = self.http.request('GET', self._base_url)
        if resp.status != 200:
            print("Status code not 200")
            exit()

        resp_data = resp.data.decode('utf-8')
        self.get_title(resp_data)
        self.get_chapter_path(resp_data)
        self.get_next_chapter_url(resp_data)
        
    def get_title(self, resp_data:str):
        title = re.search(self._rule.SEARCH_TITLE, resp_data)
        if not title:
            print("can't found title, Exit...")
            exit()

        title = title.group(1)
        idx = len(title)
        idx = title.find(self._rule.FIND_TITLE)

        self._info['title'] = title[0:idx]
        #self._info['chapter_num'] = re.search(r'(\d+)', self._info['title']).group(1)
        return

    def get_chapter_path(self, resp_data:str):
        search_image_res = re.search(self._rule.SEARCH_IMAGE_RES, resp_data, re.M|re.I)
        search_image_path = re.search(self._rule.SEARCH_IMAGE_PATH, resp_data, re.M|re.I)

        if not search_image_res or not search_image_path:
            print("can't found image path or image res, Exit...")
            exit()

        image_res:str = search_image_res.group(1)
        path:str = search_image_path.group(1)
        image_path_list:list = path[2:-1].split(",")

        index = 0
        for e in image_path_list:
            e = e.replace('"', '')
            e = e.replace('\\', '')
            image_path_list[index] = image_res + e
            index += 1

        self._info['chapter_image_url'] = image_path_list
        return
        

    def get_next_chapter_url(self, resp_data:str):
        search_next_chapter_url = re.search(self._rule.SEARCH_NEXT_URL, resp_data, re.M|re.I)

        if not search_next_chapter_url:
            print("can't found next chapter url, Exit...")
            exit()

        self._info['next_chapter_url'] = search_next_chapter_url.group(1).replace('\\', '')
        return

    def download_chapter_images(self):
        chapter_dir = os.path.join(self._base_dir, self._info['title'])
        if not os.path.exists(chapter_dir):
            os.mkdir(chapter_dir)

        for url in self._info['chapter_image_url']:
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
    
    @property
    def next_chapter_url(self):
        return self._info['next_chapter_url']

    def next_chapter(self):
        self._base_url = self.next_chapter_url
        self._info = {}
        self.get_base_message()


if __name__ == '__main__':
    manhua = DownloadManhua(download_rule.DuoDuoManHua)
    manhua.base_url = 'https://m.duoduomh.com/manhua/xuanfengguanjia/527856.html'
    manhua.base_dir = 'D:\图片\旋风管家'
    manhua.get_base_message()
    # pprint(manhua._info)

    while 1:
        manhua.download_chapter_images()
        manhua.next_chapter()
