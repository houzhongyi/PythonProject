# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class QcwyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()     #岗位名称
    amount = Field()    #招聘人数
    experience = Field()#工作经验
    company = Field()   #公司名称
    link = Field()      #公司网址
    scale = Field()     #公司规模
    salary = Field()    #岗位薪资
    updatetime = Field()#更新时间
    address = Field()   #工作地址
    jobInfo = Field()   #职位信息
    jobUrl = Field()    #职位链接
