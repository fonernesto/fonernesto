FROM mongo:latest

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev

#RUN pip3 install pymongo

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "blockchain_mongo.py" ]

EXPOSE 27017
