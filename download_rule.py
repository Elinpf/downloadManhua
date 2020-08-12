import re

class Rule():
    SEARCH_IMAGE_PATH = RuntimeError()
    SEARCH_IMAGE_RES  = RuntimeError()
    SEARCH_NEXT_URL   = RuntimeError()
    SEARCH_TITLE      = RuntimeError()
    FIND_TITLE        = None


class DuoDuoManHua(Rule):
    """
    https://m.duoduomh.com/manhua/
    """
    SEARCH_IMAGE_PATH = r'var chapterImages =(.*?);var'
    SEARCH_IMAGE_RES  = r'getCih1.*?\'(.*?)\';'
    SEARCH_NEXT_URL   = r'var nextChapterData.*?"url":"(.*?)"}'
    SEARCH_TITLE      = r'<title>(.*?)</title>'
    FIND_TITLE        = '在线'

class AcgZone(DuoDuoManHua):
    """
    https://m.acgzone.net/manhua/
    """
    SEARCH_IMAGE_RES  = r'window\[cih\].*?\'(.*?)\';'