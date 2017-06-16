import urllib2
import os
import re, json
import bs4
from bs4 import BeautifulSoup
import datetime,time
import csv
import sys
from pyquery import PyQuery as pq
import urllib2
import traceback
import requests
from datetime import timedelta,datetime
from dateutil import parser
from goose import Goose




def call_link(url,cnt): 
    link = url
    try:
        g = Goose()
        article = g.extract(url=url)
    except:
        f = open('unscraped_links.txt','a')
        f.write(link+'|')
        f.close()

    try:
        heading = article.title.encode('ascii','ignore')
    except:
        print traceback.format_exc()

    try:
        contents = article.cleaned_text.encode('ascii','ignore')
    except:
        print traceback.format_exc()

    try:
        tags = article.meta_keywords.encode('ascii','ignore')
    except:
        print traceback.format_exc()
            
    try:
        img_link = article.top_image.src
    except:
        print traceback.format_exc()
            
    try:
        description = article.meta_description.encode('ascii','ignore')
    except:
        print traceback.format_exc()
            
        
                    

    try:
        print heading
        config_file = open('conf' + str(cnt) + '.json','w')
        data = {"contents":contents , "heading": heading } 

        json.dump(data,config_file)
        #dump2db(sno,link,tags,description,img_link,contents,heading,date)
    except:
        print traceback.format_exc()
        f = open('unscraped_links.txt','a')
        f.write(link+'|')
        f.close()   
                



def call_url(url):
    try:
        con = urllib2.urlopen(url)
        html = con.read()
        s = pq(html)
        
        links = s('.newsday a')
        
        cnt = 0
        for item in links:
            
            cnt = cnt + 1
            config_file = open('conf' + str(cnt) + '.json','w')
            data = {"link": s(item).attr('href'), "heading": s(item).text() } 
            json.dump(data,config_file)
        


                
    except:
        f = open('unscraped_links.txt','a')
        f.write(url+'|')
        f.close()




if __name__ == "__main__":
    call_url("https://www.nlm.nih.gov/medlineplus/newsbydate.html")
    #call_link("http://www.livescience.com/34790-pms-symptoms-treatment-premenstrual-syndrome.html")
