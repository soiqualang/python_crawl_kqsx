# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#https://xskt.com.vn/ket-qua-xo-so-theo-ngay/mien-nam-xsmn/30-5-2019.html

class XsktItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    #save date
    xs_info=scrapy.Field()
    #save kq
    xs_data=scrapy.Field()
