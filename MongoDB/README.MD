## webscraper_Mongo

    
    
# Author: Ernest Fon Ndoh
email: fonernesto@gmail.com


# Prerequisite:
-Python (3.0+)
-python libraries:Requests==2.23.0,bs4==4.8.0

# User guide:

run command: $ python blockchain.py

output: file log.text tab delimited( when running the script, every minute you see information of the highest value on https://www.blockchain.com/btc/unconfirmed-transactions.)Columns in file: Hash, Time, BTC, USD.


# Webscraber mongoDB
#  steps:

-Install mongoDB.sh and create webscraber with a password(password)

-InstallandRun.sh then install the neccessary python libriaries then scrape blockchain.py

# blockchain.py
form and start writing to a MongoDB database. When it is running, every minute a line is added to the log file with the transaction information of the highest value in https://www.blockchain.com/btc/unconfirmed-transactions. The following transaction information are recorded:"Hash", "Time", "Amount (BTC)", "Amount (USD)" and will be stored as a json objects.

# Requirements
Firefox
Python (3.0 +)
Python Libraries: bs4, pandas,request
Ubuntu virtual machine