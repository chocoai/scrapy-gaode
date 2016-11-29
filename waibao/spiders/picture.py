# -*- coding: utf-8 -*-
import scrapy
import re
from ..pipelines import connDB


class PictureSpider(scrapy.Spider):
    name = "picture"
    allowed_domains = ["ditu.amap.com"]
    conn, cur = connDB()
    i = 0

    def start_requests(self):

        sql = "select uid, photo_urls from mianyang_sp where photo_exists = '1'"
        self.cur.execute(sql)
        data = self.cur.fetchall()

        for each in data:
            picture_str = each[1]
            picture_list = picture_str.split(' ')
            if len(picture_list) == 4:
                uid = each[0]
                url = "http://ditu.amap.com/detail/%s" % uid
                # print(url)
                yield self.make_requests_from_url(url)

    def parse(self, response):
        self.i += 1
        print(self.i)

        url = response.url
        uid = re.search("([0-9A-Z]+)", url).group(1)

        photo_urls = ""
        img_nodes = response.xpath("//div[@class='display_wrap']//li/a[@class='example-image-link']/@href")
        for img_node in img_nodes:
            img_url = img_node.extract()
            photo_urls = photo_urls + " " + img_url
        # print(photo_urls)
        sql = 'update mianyang_sp set photo_urls = "%s" where uid = %s'
        data = (photo_urls, uid)
        self.cur.execute(sql, data)
        self.conn.commit()








