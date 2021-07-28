'''
-*- coding: utf-8 -*-
@Author  : zoeyzhu
@Time    : 2021/7/19 9:31 下午
@Software: PyCharm
@email: zhuxinzhou999@zju.edu.cn
@File    : spider.py
@function:
这是一个需登录（无验证码网页爬虫的模版）


'''
import requests
from bs4 import BeautifulSoup
from http import cookies
import urllib
import http.cookiejar
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
}

session = requests.Session()
session.headers.update(headers)
url='http://bc.logistics.sinotrans.com/sco/*.login?login_name=123456&password=123456&locale=zh&referenceModel=origen'
def login(username, password):  # 模拟登入函数
    # 构造表单数据
    data = {  # 需要传去的数据
               'login_name': username,
               'password': password,
               'locale': 'zh',
            'referenceModel': 'origen'
    }
    html = session.post(url, data=data, headers=headers)

    print(html.text)



def getdata(username,password):
    login(username, password)
    login_url = 'https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check'
    per_html = session.get(login_url)
    x_html=session.get("登录后浏览器的页面")
    # soup = BeautifulSoup(per_html.text, 'lxml', from_encoding="utf-8")

    soupx = BeautifulSoup(x_html.text, 'lxml', from_encoding="utf-8")

    #根据页面标签，定位相应的数据如：
    '''
      1 = soup.find('input',id='login_name')['value']#数据
    2 = soup.find('input',id='password')['value']#密码
    '''


username=''
password=''
getdata(username,password)
# print(checkrz(username1,password1))