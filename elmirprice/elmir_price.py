#!/usr/bin/python
# -*- coding: utf-8 -*-
###
# Script to parse some categories at elmir.ua shop
# Add your own categories
###
from lxml import html
import requests
import re
import csv
import datetime
import urllib3
import openpyxl
from time import gmtime, strftime, time, localtime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
now = datetime.datetime.now()
timenow = strftime("%d%m%y_%H%M", localtime())
csv_file = 'elmir_price_' + str(timenow) + '.csv'
xls_file = 'elmir_price_' + str(timenow) + '.xls'
open(csv_file, 'w').close()

print ("Parsing")
print("----------------------------------------")
# categories - see shop website 
categories = "video_cards", "processors", "motherboards"
for url in categories:
	current_url = ('https://elmir.ua/' + url + '/?onnal=1&orderby=cost&orderdir=asc&size=500')
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(url=current_url, headers=headers, verify=False)
	tree = html.fromstring(page.content)
	items = tree.xpath('//a[@class="item-name"]/text()')
	raw_prices = tree.xpath('//span[@class="price cost"]/text()')
	item_url =  tree.xpath('//p[@class="name"]//a/@href')
	prices = [re.sub('\\xa0грн', '', i) for i in raw_prices]
	print(url, " - processed")

	with open(csv_file, 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(["Price from", now.strftime("%Y-%m-%d %H:%M"), ""])
		spamwriter.writerow(["Item Name ", "Item Price", "Item Url"]) 
		data = list(zip(items, prices, item_url))
		for row in data:
			row = list(row)
			spamwriter.writerow(row)
		spamwriter.writerow([])
print("----------------------------------------")
print("Parsed and written to - csv file: ", csv_file)

csv_parsed = open(csv_file)
wb = openpyxl.Workbook()
ws = wb.active
reader = csv.reader(csv_parsed, delimiter=',')
for i in reader:
    ws.append(i)
csv_parsed.close()
wb.save(xls_file)
print("Parsed and written to - xls file: ", xls_file)
