# encoding:utf-8
#网页屏蔽，服务器屏蔽

import urllib2
# def download1(url):
#     return urllib2.urlopen(url).read() #读取全部网页
#
# url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&p=1&isadv=0" #urlopen只能处理http.不可以处理https
# print download1(url)

import selenium
import selenium.webdriver
import re

def getnumbername(searchname):
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&kw=java&p=1&isadv=0"
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    pagesource = driver.page_source #抓取网页源代码
    restr = "<em>(\\d+)</em>"
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(pagesource)
    driver.close()
    return mylist[0]

pythonlist = ["python","python运维","python测试","python数据","python web"]
for i in pythonlist:
    print i,getnumbername(i)



