# A python spider

## 简介

一个爬虫引擎，用来获取不需要登录的页面的内容，可以不断递归抓取，内部已经封装好，可以拿去直接多开一些线程抓取

## 需要自行修改的地方

root_url：开始爬取的url
内容用正则表达式匹配，具体内容自行修改

## 文件说明：

* spider_main.py：爬虫主调度程序
* url_manager : url管理器,用来调用和添加url
* html_downloader.py：html下载器，用来下载网页的内容
* html_parser：html解析器，用来搜索要抓取的内容
* html_outputer：html输出器，输出获得的数据内容