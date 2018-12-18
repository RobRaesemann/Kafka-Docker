from kafka import KafkaProducer
from kafka import KafkaConsumer

# producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
# for _ in range(100):
#    producer.send('foobar', b'some_message_bytes')


consumer = KafkaConsumer('foobar', auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
print('waiting')
for msg in consumer:
    print (f'message: {msg}')

print('done')