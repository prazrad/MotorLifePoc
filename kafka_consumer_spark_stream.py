import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pymongo
import json
import ast
import configparser

# Read configurations from config.txt file
config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))
mongoConn = config.get('MongoDB', 'mongoConn')
db = config.get('MongoDB', 'db')
coll = config.get('MongoDB', 'coll')

#Insert Record to MongoDB
def insertRecord(data):
   dict = ast.literal_eval(data)

   #Calculate life
   if dict['temperature']>=80 and dict['temperature']<=100:
       dict['life']=10
   elif dict['temperature']>100:
       dict['life']=5
   else:
       dict['life']=None

   myclient = pymongo.MongoClient(mongoConn)
   mydb = myclient[db]
   mycol = mydb[coll]

   mycol.insert_one(dict)

if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingKafka")
    ssc = StreamingContext(sc, 2)
    brokers, topic = sys.argv[1:]
    kfk = KafkaUtils.createDirectStream(ssc, [topic],{"metadata.broker.list": brokers})

    data = kfk.map(lambda x: insertRecord(x[1]))
    data.pprint()

    ssc.start()
    ssc.awaitTermination()
