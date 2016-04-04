# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import csv
from hltv import settings

class HltvPipeline(object):
	def __init__(self):
		self.csvwriter = csv.writer(open('out.csv', 'wb'))
		self.csvwriter.writerow(['MatchLink','Date','Map','Team 1','Team 1 Score','Team 2','Team 2 Score','Event','Team 1 Link', 'Team 2 Link','Event Link'])

	def process_item(self, item, spider):
		self.csvwriter.writerow([item['matchLink'][0], item['date'][0], item['mapName'][0], item['team1'][0], item['team1Score'][0], item['team2'][0], item['team2Score'][0], item['event'][0], item['team1Link'][0], item['team2Link'][0], item['eventLink'][0]])
		return item