# -*- coding=utf-8 -*-
#引入selenium
import csv
import time
import jieba
from selenium import webdriver

web = webdriver.Chrome() #打开谷歌浏览器
web.get('https://login.51job.com/login.php?lang=c') #在浏览器地址栏把网址加入

web.find_element_by_xpath('//*[@id="loginname"]').send_keys('19971660997') #输入账号
web.find_element_by_xpath('//*[@id="password"]').send_keys('127128617623zyq') #输入密码

#点击登录
web.find_element_by_xpath('//*[@id="login_btn"]').click()
#全屏最大化浏览器
web.maximize_window()

web.find_element_by_xpath('//*[@id="topIndex"]/div/p/a[2]').click() #点击“职位搜索”
#找到搜索框，输入要搜索的关键字
web.find_element_by_xpath('//*[@id="kwdselectid"]').send_keys('新媒体广告')

web.find_element_by_xpath('//*[@id="work_position_input"]').click() #点击选择地区

ttags = web.find_elements_by_class_name('ttag') #我们这里选择全国范围的职位，把单个城市的选项取消。找到每个城市的class标签，发现=ttag
#依次点击所有的tag，来删掉单个城市
for tag in ttags:
    tag.click()

#点击确定
web.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()
#点击搜索
web.find_element_by_xpath('/html/body/div[2]/form/div/div[1]/button').click()

num = 0
while num < 3:
    #找到搜索的全部内容
    lst = web.find_element_by_xpath('//*[@id="resultList"]').find_elements_by_class_name('el')

    f = open("companyInformation.csv",mode="a")#打开一个文件来存放下面的数据； 文件格式为：数据，数据，数据     a表示追加
    for el in lst:
        if "title" not in el.get_attribute('class'):
            job_name = el.find_element_by_class_name('t1').text
            company_name = el.find_element_by_class_name('t2').text
            job_address = el.find_element_by_class_name('t3').text
            salary = el.find_element_by_class_name('t4').text
            data = el.find_element_by_class_name('t5').text

            f.write(job_name)
            f.write(',')
            f.write(company_name)
            f.write(',')
            f.write(job_address)
            f.write(',')
            f.write(salary)
            f.write(',')
            f.write(data)
            f.write('\n') #换行

    web.find_element_by_xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[last()]/a').click()
    time.sleep(1)
    num += 1

f1 = open('D:\pyProject\\companyInformation.csv').read().split('\n') #一行行的读
List1 = [] #建立储存分词的列表
for i in range(len(f1)):
    result = []
    seg_list = jieba.cut(f1[i])
    for w in seg_list: #读取每一行分词
        result.append(w)
    List1.append(result)#将该行分词写入列表形式的总分词列表
#写入CSV
f2 = open('D:\pyProject\\afterJIEBA.csv','w')
writer = csv.writer(f2)#定义写入格式
writer.writerows(List1)#按行写入
f2.close()