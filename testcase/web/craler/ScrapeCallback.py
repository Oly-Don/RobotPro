# -*- coding=utf-8 -*-

class ScrapeCallbac:
    def __init__(self):
        print '=======ScrapeCallbac Call============'

    # 回调函数
    def __call__(self, *args, **kwargs):
        print '=======ScrapeCallbac Call============'
