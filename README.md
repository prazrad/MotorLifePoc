# MotorLifePoc
POC to determine the life of Motor based on the sensor data

### Python Required Lib - configparser
```pip3 install configparser```

### Configuration - Connection Parameters
Update the connection parameters of Kafka and MongoDB in the **config.txt** file

### Start the Data Generation and Kafka Consumer
```python3 data_gen_kafka_producer.py```

### Start Spark Streaming Job
```./spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 kafka_consumer_spark_stream.py localhost:9092 sensor```



