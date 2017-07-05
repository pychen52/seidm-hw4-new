# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CwbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sid = scrapy.Field()
    t_10m = scrapy.Field()
    t_1h = scrapy.Field()
    t_3h = scrapy.Field()
    t_6h = scrapy.Field()
    t_12h = scrapy.Field()
    t_24h = scrapy.Field()
    t_today = scrapy.Field()
    t_yday = scrapy.Field()
    t_2d = scrapy.Field()
    update_time = scrapy.Field()