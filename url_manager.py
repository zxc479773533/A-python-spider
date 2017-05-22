# url管理器，用来调用和添加url
class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向集合添加新的一个不重复的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    # 确定集合是有待处理的url
    def has_new_url(self):
        return len(self.new_urls) != 0
    
    # 获取新的待处理的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    # 添加新的url，调用添加单个url的函数实现
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)