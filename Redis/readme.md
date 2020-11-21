# WebScraperMongoDB
Prerequisits:
Firefox
Python (3.0 +)
Python Libraries: selenium, bs4, pandas
Ubuntu

# Guide:
Run the Installed redis.sh bash script from the WebScraperMongoDB . This will run the MongoDB.sh and MongoDB.py scripts.

Configure redish.sh
Installs MongoDB and creates a user webscraber

Installs the necessary python libraries. It will starts BlockChainScraper MongoDB.py.It will also write to mongoDb database.Every minute a line will be added to the log with the transaction information of the highest value transaction listed on the site https://www.blockchain.com/btc/unconfirmed-transactions.These  transaction will be recorded in "Hash", "Time", "Amount (BTC)", "Amount (USD)". The records are stored in a jason format.




