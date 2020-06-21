from kafka import KafkaProducer
import time
import uuid
import random
import datetime
import json
import configparser

# Read configurations from config.txt file
config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))
bootstrapConn = config.get('Kafka', 'bootstrapSvr')

# Setup the Kafka producer connection
producer = KafkaProducer(bootstrap_servers=bootstrapConn)

# Data generator - Simulating the Sensor data
while True:
  time.sleep(3)
  data = {
  'id':str(uuid.uuid1()),
  'machineId':random.randint(1000,1010), #Generating data for 10 machines
  'datetime':str(datetime.datetime.now()),
  'temperature':random.randint(80,120),
  'motorRPM':random.randint(2000,2500)
  }
  print(data)
  #Send data to topic 'sensorRaw'
  producer.send('sensorRaw', json.dumps(data).encode('utf-8'))
