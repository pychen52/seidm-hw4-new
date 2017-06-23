# -*- coding: utf-8 -*-
import scrapy
from cwb.items import CwbItem

class A136Spider(scrapy.Spider):
    name = 'a136'
    allowed_domains = ['www.cwb.gov.tw']
    start_urls = ['http://www.cwb.gov.tw/V7/observe/rainfall/A136.htm']

    def parse(self, response):
        item = CwbItem()
        for station in response.css('tr.Area3'):
            item['name'] = station.css('td span::text').re("[\u4e00-\u9fa5]{1,}")[0]
            item['sid'] = station.css('td span::text').re("[A-Z0-9]{5,}")[0]
            item['t_10m'] = station.css('td font::text').extract()[0]
            item['t_1h'] = station.css('td font::text').extract()[1]
            item['t_3h'] = station.css('td font::text').extract()[2]
            item['t_6h'] = station.css('td font::text').extract()[3]
            item['t_12h'] = station.css('td font::text').extract()[4]
            item['t_24h'] = station.css('td font::text').extract()[5]
            item['t_today'] = station.css('td font::text').extract()[6]
            item['t_yday'] = station.css('td font::text').extract()[7]
            item['t_2d'] = station.css('td font::text').extract()[8]
            yield item
