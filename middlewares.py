# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random



# 预定义的PC端用户代理列表
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # ... 添加更多用户代理 ...
]


def random_user_agent():
    return random.choice(USER_AGENTS)


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 这里可以修改请求或执行其他操作
        # 在请求头中设置随机的用户代理
        request.setdefault('User-Agent', random_user_agent())
        print("111111111111111111111111111111")
        print(f"Request URL: {request.url}")

    def process_response(self,request, response, spider):
        # Called with the response returned from the downloader.
        print("111111111111111111111111111111" + request.headers)
