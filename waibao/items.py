# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class GaoDeItem(Item):
    uid = Field()  # 高德上的id
    name = Field()
    address = Field()
    tag = Field()
    sub_tag = Field()
    center = Field()
    tel = Field()
    pro_name = Field()
    pro_center = Field()
    city_name = Field()
    city_center = Field()
    ad_name = Field()
    ad_center = Field()
    street_name = Field()
    street_center = Field()
    distance = Field()
    photo_urls = Field()
    photo_exists = Field()
