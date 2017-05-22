# url下载器，用来从网上下载对应的网页内容
from urllib import request

class HtmlDownloader(object):

    def download(cls, url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()