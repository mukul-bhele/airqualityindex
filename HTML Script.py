# -*- coding: utf-8 -*-
'''
The provided Python script is designed to retrieve HTML data from a weather website (http://en.tutiempo.net/) for a specific location with the identifier 
ws-421820'. The code iterates over the years 2013 to 2018 and, for each year, iterates over the months from January to December. It dynamically generates
URLs for each month and year, then uses the 'requests' library to fetch the HTML content from the corresponding webpage. The retrieved HTML data is then
stored in separate files organized by year and month in the "Data/Html_Data" directory. If the directory for a particular year doesn't exist, it is created.

In summary, the script automates the process of fetching historical weather data HTML pages for different months and years and organizes the data in a
structured directory for subsequent analysis. The total time taken for the data retrieval process is printed at the end.
'''
import os
import time
import requests
import sys


def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))
        
    
