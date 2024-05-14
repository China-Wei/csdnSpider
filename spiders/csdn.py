import html2text
import scrapy

class CustomHTML2Text(html2text.HTML2Text):
    def handle_img(self, tag, attrs):
        """Overwrite the default handle_img method to output the img tag as text."""
        # Reconstruct the img tag as text
        attrs_str = ' '.join(f'{k}="{v}"' for k, v in attrs.items())
        return f"<img {attrs_str}>"

class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = ["https://blog.csdn.net/I_am_sold_out/article/details/113818985"]

    def parse(self, response):
        # 保存一份html页面
        with open('csdn.html', 'wb') as f:
            f.write(response.body)
        # 设置断点
        #   解析xpath
        cotent_node = response.xpath('//*[@id="content_views"]').get()
        # 创建html2text对象并转换HTML
        text_converter = CustomHTML2Text(bodywidth=2000)
        text_converter.images_as_html = True

        # text_converter.ignore_links = True
        converted_text = text_converter.handle(cotent_node)
        print(converted_text)
        pass
