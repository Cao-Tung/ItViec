# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItviecItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    job = scrapy.Field()
    area = scrapy.Field()
    salary = scrapy.Field()
    exp = scrapy.Field()
    quantum = scrapy.Field()
    description = scrapy.Field()
    benefit = scrapy.Field()
    require = scrapy.Field()
    cv = scrapy.Field()
    addresscompany = scrapy.Field()
    deadline = scrapy.Field()
    skill = scrapy.Field()
