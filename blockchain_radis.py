from os import path
import requests 
from bs4 import BeautifulSoup 
import time
import redis


def scrap_bloackchain():
    
    # list to store the max value hash inforamtion
    hash_list = [0]*4
    max_amount = -99999999
    
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('div', attrs = {'class':'sc-1g6z4xm-0'})
    # loop over all div tags for each hash row
    i = 0
    
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
            rkey = 'k' + str(i)
            redis_db.hset(rkey, hash_data)
            i = i + 1

    return i

        
if __name__ == "__main__":

    # redis config
    redis_host = "127.0.0.1"
    redis_port = 6379
    redis_password = ""
    redis_db = redis.Redis(host=redis_host, port=redis_port)
    
    starttime = time.time()
    i = 0
    while True:
        print("after {} min(s)".format(i))
        count = scrap_bloackchain()
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        print("{} records written to redis db".format(count))
        i+=1
