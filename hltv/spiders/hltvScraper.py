import scrapy

from hltv.items import HltvItem

class HltvSpider(scrapy.Spider):
    name = "hltv"
    allowed_domains = ["hltv.org"]
    start_urls = [
        "http://www.hltv.org/?pageid=188&offset=0",
    ]

    def parse(self, response):
        for sel in response.xpath('//div[contains(@style,"padding-left:5px;padding-top:5px;")]'):
            item = HltvItem()

            item['date'] = sel.xpath('a[contains(@href,"matchid")]/div/text()').extract()
            item['matchLink'] = sel.xpath('a[contains(@href,"matchid")]/@href').extract()
            item['team1'] = sel.xpath('a[contains(@href,"teamid")][1]/div/text()').re('\s*(.*)\s\(')
            item['team1Score'] = sel.xpath('a[contains(@href,"teamid")][1]/div/text()').re('\((\d+)\)$')
            item['team1Link'] = sel.xpath('a[contains(@href,"teamid")][1]/@href').extract()
            item['team2'] = sel.xpath('a[contains(@href,"teamid")][2]/div/text()').re('\s*(.*)\s\(')
            item['team2Score'] = sel.xpath('a[contains(@href,"teamid")][2]/div/text()').re('\((\d+)\)$')
            item['team2Link'] = sel.xpath('a[contains(@href,"teamid")][2]/@href ').extract()
            item['mapName'] = sel.xpath('div[contains(@style,"font-weight:normal;width:9%;float:left;text-align:center;font-weight:normal;color:black;")]/text()').extract()
            item['eventLink'] = sel.xpath('a[contains(@href,"eventid")]/@href').extract()
            item['event'] = sel.xpath('a[contains(@href,"eventid")]/div/div/text()').extract()
            yield item

#Base:               //div[contains(@style,"padding-left:5px;padding-top:5px;")]
#Date                a[contains(@href,"matchid")]/div/text()          .extract()
#Matchlink:          a[contains(@href,"matchid")]/@href               .extract()
#team1:              a[contains(@href,"teamid")][1]/div/text()        .re('\s*(.*)\s\(')
#team1 Score:        a[contains(@href,"teamid")][1]/div/text()        .re('\((\d+)\)$')
#team1Link:          a[contains(@href,"teamid")][1]/@href             .extract()
#team2:              a[contains(@href,"teamid")][2]/div/text()        .re('\s*(.*)\s\(')
#team2 Score:        a[contains(@href,"teamid")][2]/div/text()        .re('\((\d+)\)$')
#team2Link:          a[contains(@href,"teamid")][2]/@href             .extract()
#mapName             div[contains(@style,"font-weight:normal;width:9%;float:left;text-align:center;font-weight:normal;color:black;")]/text()            .extract()
#event               a[contains(@href,"eventid")]/@href               .extract()
#eventLink           a[contains(@href,"eventid")]/div/div/text()      .extract()

