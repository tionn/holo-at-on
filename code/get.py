# -*- coding: utf-8 -*-

import os
import io
import urllib2
import string
from BeautifulSoup import BeautifulSoup
import pandas as pd
import sys

city_url = 'http://twblg.dict.edu.tw/holodict_new/index/xiangzhen_level1.jsp?county=1'

def extract_items(base_url):	
	html = urllib2.urlopen(base_url).read()
	soup = BeautifulSoup(html)
	#print(soup.prettify())

	data = []	
	table = soup.findAll('tr', attrs={'class':['all_space1', 'all_space2']})	

	for row in table:
		cols = row.findAll('td')
		cols = [ele.text.strip() for ele in cols]
		data.append([ele for ele in cols if ele]) # Get rid of empty values	
	
	return data


def get_area_url():
	base_url = 'http://twblg.dict.edu.tw/holodict_new/index/xiangzhen_level1.jsp?county=%s'
	url = []
	for i in string.ascii_uppercase:
		url.append(base_url % i)	
	return url


if __name__=='__main__':
	# 縣市名稱	
	data = extract_items(city_url)
	data.pop() # ignore data from '其他'
	print 'Cities and countries are done.'			

	# 鄉鎮區名稱
	area_url = get_area_url()
	for i in area_url:
		area_data = extract_items(i)
		data.extend(area_data)		

	print 'Townships are done.'

	#df = pd.DataFrame(data, columns=['name', 'holo'])	
	df = pd.DataFrame(data)		
	df.to_csv('moe_mapping.csv', encoding='utf-8', index=False, header=0)
	print 'csv file done.'