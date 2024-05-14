# -*- coding: utf-8 -*-
# @Time     : 2019/04/03
# @Author   : sxz


from scrapy import cmdline

name = 'csdn'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
