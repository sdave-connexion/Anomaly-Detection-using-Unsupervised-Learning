#Importing the required libraries

import os
import time
import csv
import requests
from bs4 import BeautifulSoup

#code to scrape from the created web server

while True:
    data = requests.get('http://192.168.4.1/') 
    soup = BeautifulSoup(data.text,'lxml')
    rows = soup.find('h1')
    Scaped_Column = rows.text.split(';') 
    print (time.strftime('%Y-%m-%d %H:%M:%S'),Scaped_Column)
    f=open("/home/pi/data_collection.csv",'a',newline='')
    c=csv.writer(f,delimiter=' ')
    c.writerow('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}'.format(time.strftime('%Y-%m-%d %H:%M:%S'),Scaped_Column[0],Scaped_Column[1],Scaped_Column[2],Scaped_Column[3],Scaped_Column[4],Scaped_Column[5],Scaped_Column[6],Scaped_Column[7],Scaped_Column[8],Scaped_Column[9],Scaped_Column[10],Scaped_Column[11]))
    time.sleep(60)
f.close()


