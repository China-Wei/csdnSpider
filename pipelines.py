# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logger
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CsdnspiderPipeline:
    def __init__(self):
        self.file = None

    # def open_spider(self, spider):
    #     if spider.name == 'csdn':
    #         self.file = open("csdntemp.md", 'w', encoding='GBK')

    def process_item(self, item, spider):
        if spider.name == 'csdn':
            item = dict(item)
            title = item['title'] + ".md"
            self.file = open(title, 'w', encoding='UTF-8 ')
            self.file.write(item['content'])
            self.file.close()
        return item

    # def close_spider(self, spider):
    #     if spider.name == 'csdn':
