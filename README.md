# MotorLifePoc
POC to determine the life of motor based on the sensor data

This is an simulated experiement to find the remaining life of indusrial equipments. In real world it depends up on various industrial factors and data collected by the sensor.

Over all flow of the POC (High-level architecture):

![High-level Architecture](https://i.imgur.com/y9QXksC.png)

### Kafka Installation
1. Download Apache Kafka from [here.](https://www.apache.org/dyn/closer.cgi?path=/kafka/) After downloading, unzip the file and open the kafka directory in the terminal.

2. Start zookeeper server:
```bin/zookeeper-server-start.sh config/zookeeper.properties```

3. Start kafka server:
```bin/kafka-server-start.sh config/server.properties```

For more info - Kafka official documentation is [here.](https://kafka.apache.org/quickstart)


After cloning this repo performing the following :

### Python Required Lib - configparser
```pip3 install configparser```

### Configuration - Connection Parameters
Update the connection parameters of Kafka and MongoDB in the **config.txt** file

### Start the Data Generation and Kafka Producer
```python3 data_gen_kafka_producer.py```

### Start Spark Streaming Job
```./spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 kafka_consumer_spark_stream.py localhost:9092 sensorRaw```

Parameter "sensorRaw" is the kafka topic name.

### Results
The data generated is populated under the mongoDB collection along with the processed value **life** of each entry with motorId. Using the data analytics and visualization tools we can view the data for health monitoring and checking the life of motors.


