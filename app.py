#libraries imports
import requests
import json
from bs4 import BeautifulSoup as BS
from datetime import datetime, timedelta
import csv

#configuring request header
headers = {
    "user-agent":'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)'
    }



def GetPage():
    url = "https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm"   #link
    page = requests.get(url, headers = headers)             

    page_content = BS(page.content, 'html.parser')          #page content

    result = page_content.find_all("tr")                    #table row data from page

    final_dict = {}
    final_list = []

    for item in result:
        date = item.find("td", {"class":"B6"})              #table data with class B6 for date
        prices = item.find_all("td", {"class":"B3"})        #table data with class B3 for prices
        

        #
        if date is not None:
            wk_date = date.text     
            wk_date = wk_date.replace("\xa0\xa0", "")       #remove unwanted characters
            wk_price = []
            for price in prices:
                new_price = price.text
                wk_price.append(new_price)
                
            
            next_five_days = sortDate(wk_date)
            for idx, date in enumerate(next_five_days):
                price = wk_price[idx]
                day_price_dict = {date: price}
                day_price_list = [date, price]
                final_dict.update(day_price_dict)
                final_list.append(day_price_list)

    sendToExcel(final_list)


def sortDate(wk_date):
    next_five_days = []
    re_date = wk_date.split(" to ")

    st_date = re_date[0]
    new_date = ''
    if st_date[-2] == ' ':
        my_date = datetime.strptime(st_date, "%Y %b- %d").date()
        new_date = my_date
        

    else:
        my_date = datetime.strptime(st_date, "%Y %b-%d").date()
        new_date = my_date


    start_day = new_date.day
    

    for i in range(0, 5):
        next_day = new_date + timedelta(days=i)
        next_five_days.append(str(next_day))

    return next_five_days


        
def sendToExcel(price_data):
    csv_head = ["Date","Price (Dollars per Million Btu)"]

    try:

        with open('datapackage/Henry Hub Daily-gas-prices.csv', 'w', newline='', encoding='utf-8') as gasPrice:
            write = csv.writer(gasPrice)
            write.writerow(csv_head)
            write.writerows(price_data)

        print("Done!")
    
    except Exception as error:
        print("Error!", str(error))
    

    
GetPage()
