# url解析器
from bs4 import BeautifulSoup
import re
from urllib import parse

class HtmlParser(object):
    # 解析网页的DOM对象
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    # 获得下一个url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 用正则表达式匹配对应要搜索的下一级链接
        links = soup.find_all('a', href = re.compile(r"/item/")) # 这里填上要匹配的链接
        # 将该网页的链接添加到集合里等待以后调用
        for link in links:
            new_url = link['href']
            # 让 new_url 以 page_url 为模板拼接成一个全新的 url
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls
    
    # 获取网页上的数据
    def _get_new_data(self, page_url, soup):
        # 创建数据集合
        res_data = {}
        # url
        res_data['url'] = page_url
        # 根据对象属性找数据
        title_node = soup.find('dd', class_= "lemmaWgt-lemmaTitle-title") # 具体内容可随意修改
        res_data['title'] = title_node.get_text()
        # 根据对象属性找数据
        summary_node = soup.find('div', class_= "lemma-summary") # 具体内容可随意修改
        res_data['summary'] = summary_node.get_text()

        return res_data