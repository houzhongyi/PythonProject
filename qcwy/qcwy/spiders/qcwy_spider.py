# # import logging
import importlib
import scrapy
import re
# import urllib
# # import codecs
# #
from scrapy.selector import Selector
#
from qcwy.items import QcwyItem

import sys
#
importlib.reload(sys)
is_start_page = True
#
#
class TestfollowSpider(scrapy.Spider):
    name = "qcwysearch"
    allowed_domains = ["51job.com"]
    start_urls = [
        # "http://search.51job.com/list/230300,000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=150200&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    ]

    def parse(self, response):
        global is_start_page

        url = ""
        # 从开始页面开始解析数据，开始页面start_urls
        if is_start_page:
            url = self.start_urls[0]
            is_start_page = False
        else:
            href = response.xpath('//div[@class="dw_page"]/ul/li[last()]/a/@href')
            url = response.urljoin(href.extract())

        yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):

        for sel in response.xpath('//div[@id="resultList"]/div[@class="el"]'):
            item = QcwyItem()
            joburl = sel.xpath('p/span/a/@href').extract()[0]
            item['title'] = sel.xpath('p/span/a/@title').extract()[0]
            item['link'] = sel.xpath('span[@class="t2"]/a/@href').extract()[0]
            item['jobUrl'] = joburl
            item['company'] = sel.xpath('span[@class="t2"]/a/text()').extract()[0]
            try:
                item['salary'] = sel.xpath('span[@class="t4"]/text()').extract()[0]
            except:
                item['salary'] = ""
            item['updatetime'] = sel.xpath('span[@class="t5"]/text()').extract()[0]
            item['address'] = sel.xpath('span[@class="t3"]/text()').extract()[0]
            yield scrapy.Request(joburl, meta={"item": item}, callback=self.get_job_content)

        next_page = response.xpath('//div[@class="p_in"]/ul/li[last()]/a/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_dir_contents)

    def get_job_content(self, response):
        item = response.meta['item']
        sel = response.xpath('//div[@class="tCompany_center clearfix"]')
        try:
            item['experience'] = sel.xpath('//div[@class="jtag inbox"]/div[@class="t1"]/span[1]/text()').extract()[0]
        except:
            item['experience'] = ""
        try:
            item['education'] = sel.xpath('//div[@class="jtag inbox"]/div[@class="t1"]/span[2]/text()').extract()[0]
        except:
            item['education'] = ""
        try:
            scale = sel.xpath('//p[@class="msg ltype"]/text()').extract()[0]
            item['scale'] = scale.strip().replace("\t", "").replace("\xa0", "").replace(" ", "")
        except:
            item['scale'] = ''
        try:
            item['amount'] = sel.xpath('//div[@class="jtag inbox"]/div[@class="t1"]/span[3]/text()').extract()[0]
        except:
            item["amount"] = ''
        try:
            temp = sel.xpath('//div[@class="bmsg job_msg inbox"]').extract()[0]
            reg = re.compile(r'<div class="bmsg job_msg inbox">(.*?)<div class="mt10">', re.S)
            jobInfo = re.findall(reg, temp)[0]
            item['jobInfo'] = jobInfo.strip().replace("<p>", "").replace("</p>", "").replace("<br>", "")\
                .replace("\xa0", "").replace("<span>", "").replace("</span>", "").replace("<b>", "").replace("</b>", "")
        except:
            item['jobInfo'] = ''
        yield item
