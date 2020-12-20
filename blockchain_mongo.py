from os import path
import requests 
from bs4 import BeautifulSoup 
import time
from pymongo import MongoClient


def scrap_bloackchain():
    
    # list to store the max value hash inforamtion
    hash_list = [0]*4
    max_amount = -99999999
    
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('div', attrs = {'class':'sc-1g6z4xm-0'})
    # loop over all div tags for each hash row
    for tr in table:
        row = tr.findAll('div', attrs = {'class':'sc-6nt7oh-0 kduRNF'}) # read each column in the div

        # convert USD from string into float
        current_USD = float(row[3].text.strip('$').replace(",", ""))

        if current_USD >= max_amount:
            max_amount = current_USD
            hash_list[0] = row[0].text
            hash_list[1] = row[1].text
            hash_list[2] = row[2].text
            hash_list[3] = '$' + str(current_USD) # convert string to list to easily join using join command
            
            hash_data = {
                'Hash': row[0].text,
                'Time': row[1].text,
                'Amount(BTC)': row[2].text,
                'Amount(USD)': '$' + str(current_USD)
            }

            result = mongo_db.insert_one(hash_data)

        
if __name__ == "__main__":
    #log_file = "log.txt"

    # create mongo db
    client = MongoClient()
    client = MongoClient('localhost', 27017, )
    db = client['blockchain']
    mongo_db = db.hashs
    
    starttime = time.time()
    i = 0
    while True:
        print("after {} min(s)".format(i))
        scrap_bloackchain()
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        i+=1
