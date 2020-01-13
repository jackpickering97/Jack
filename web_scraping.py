# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:15:09 2020

@title: HTML Scraping
@author: JackPickering
"""
#%% 
from bs4 import BeautifulSoup as bs
import requests
import os

URL_list = ['https://www.bbc.co.uk/news', 
            'https://edition.cnn.com/',
            'https://www.dailymail.co.uk/home/index.html',
            'https://www.independent.co.uk/']


def web_scrape():
    cwd = os.getcwd()
    f = open(cwd + r'\titles.txt','w')
    for i in range(len(URL_list)):
        r = requests.get(URL_list[i])
        soup = bs(r.text, 'html.parser')
        
        tag = 'title'
        table_soup = soup.find(tag)
        
        f.write(table_soup.string + '\n')
    f.close()

web_scrape()