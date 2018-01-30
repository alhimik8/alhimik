#!/usr/bin/python
# -*- coding: utf-8 -*-
###
# Skript to parse come categories at elmir.ua shop
# Add your own categories to "urls"
###
from lxml import html
import requests
import re
import csv
import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
now = datetime.datetime.now()
print ("Parsing")
print("----------------------------------------")
# categories - see shop website 
urls = "video_cards", "processors", "motherboards"
for url in urls:
	cur_url = ('https://elmir.ua/' + url + '/?onnal=1&orderby=cost&orderdir=asc&size=500')
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(url=cur_url, headers=headers, verify=False)
	tree = html.fromstring(page.content)
	items = tree.xpath('//a[@class="item-name"]/text()')
	raw_prices = tree.xpath('//span[@class="price cost"]/text()')
	prices = [re.sub('\\xa0грн', '', i) for i in raw_prices]
	print(url, " - processed")

	with open('elmir_price.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(["Price from", now.strftime("%Y-%m-%d %H:%M")])
		spamwriter.writerow(["Item Name ", "Item Price"]) 
		data = list(zip(items, prices))
		for row in data:
			row = list(row)
			spamwriter.writerow(row)
		spamwriter.writerow([])
print("----------------------------------------")
print("Parsed and written to - elmir_price.csv ")

