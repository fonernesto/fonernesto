from os import path
import requests 
from bs4 import BeautifulSoup 
import time
import redis


def scrap_bloackchain(log_file, r):
    
    # list to store the max value hash inforamtion
    hash_list = [0]*4
    max_amount = -99999999
    
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('div', attrs = {'class':'sc-1g6z4xm-0'})
    # loop over all div tags for each hash row
	i=0
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
            r.mset(rkey, hash_data)
			i++

    # ensure we only write to file if there is valid hash
    if hash_list[0] != 0:
        f=open(log_file, "a+")
        line = '\t'.join(hash_list) # combine list elements into a string to write to log file
        f.write(line + "\n") # use this for windows machine


        
if __name__ == "__main__":

    # redis config
	redis_host = "localhost"
	redis_port = 6379
	redis_password = ""
	#r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    r = redis.Redis()
    
    # create/open log file for append mode
    log_file = "log.txt"
    
    # if log file does not exist create it and write headers
    if path.isfile(log_file) != True:
        f=open(log_file,"w+")
        f.write("Hash\tTime\tAmount(BTC)\tAmount(USD)\n")
        f.close()
    
    starttime = time.time()
    i = 0
    
    while True:
        print("after {} min(s)".format(i))
        scrap_bloackchain(log_file, redis_hash)
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        i+=1
        
    
