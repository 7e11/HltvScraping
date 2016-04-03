# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HltvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    matchLink = scrapy.Field()
    team1 = scrapy.Field()
    team1Score = scrapy.Field()
    team1Link = scrapy.Field()
    team2 = scrapy.Field()
    team2Score = scrapy.Field()
    team2Link = scrapy.Field()
    mapName = scrapy.Field()
    event = scrapy.Field()
    eventLink = scrapy.Field()