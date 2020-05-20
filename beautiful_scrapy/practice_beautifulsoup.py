# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:58:21 2020

@author: Moeed
"""

from urllib.request import urlopen as uReq #package to monitor url
from bs4 import BeautifulSoup as soup #import beautiful soup
quotes_page='https://bluelimelearning.github.io/my-fav-quotes/' ## variable with web title name
uclient=uReq(quotes_page)#uclient is varibale thtough which we read the quote page and open a connection
page_html=uclient.read()#Read the web page
uclient.close()#clsoe connection
page_soup=soup(page_html,"html.parser")#Parser html so it can be understand by human
quotes=page_soup.findAll("div",{"class":"quotes"})#find all quotes in page_soup 
print (quotes[0].text.strip())

for quote in quotes:
    fav_quote=quote.findAll("p",{"class":"aquote"})
    aquote=fav_quote[0].text.strip()
    
    fav_authors=quote.findAll("p",{"class":"author"})
    author=fav_authors[0].text.strip()
    
   #print (aquote +"\n")
   #print (author)