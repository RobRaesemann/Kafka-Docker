# Kafka-Docker
This docker-compose file will start up a Kafka instance for testing.

### Make sure to create a hosts file entry for kafkaserver

```
127.0.0.1	kafkaserver
```

Kafka will automatically create a topic if you produce data to it.

Stop and start commands must be entered from the directory containing the docker-compose.yaml fle.

To start the container
``` 
docker-compose up 
```

To stop the container
```
docker-compose down
```


The docker-compose image also contains the Kafka Manager Web Console. You can access it on http port 9000

```
http://localhost:9000
```

The Kafka Tool available at http://kafkatool.com/ is also helpful for troubleshooting.

The test_kafka_consumer.py and test_kafka_producer.py files contain example Python code.