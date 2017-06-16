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
        #print s
        li = s('p')
        lk = s('a')

        names = []
        links = []   

        cnt = 0
        for item in lk:
            link = s(item).attr("href")
            if "www.myhealthnewsdaily.com" in link:
                #print link
                cnt = cnt + 1
                links.append(link)
                if cnt == 56:
                    call_link(link,cnt)
                
        
        cnt = 0
        for item in li:
            cnt = cnt + 1
            if cnt >2 :
                names.append(s(item).text())
            #print s(item).text()

                    
                
    except:
        f = open('unscraped_links.txt','a')
        f.write(url+'|')
        f.close()




if __name__ == "__main__":
    call_url("http://www.livescience.com/36519-diseases-conditions-symptoms-treatments.html")
    #call_link("http://www.livescience.com/34790-pms-symptoms-treatment-premenstrual-syndrome.html")
