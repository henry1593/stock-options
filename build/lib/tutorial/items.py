# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    optionschain = scrapy.Field()
    strikeprice=scrapy.Field()
    lastprice = scrapy.Field()
    volume = scrapy.Field()
    todaysdate=scrapy.Field()

    pass
