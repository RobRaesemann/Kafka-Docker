from kafka import KafkaProducer
from kafka import KafkaConsumer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
for x in range(100):
    print(f'sending {x}')
    key_bytes = bytes(f'key{x}', encoding='utf-8')
    value_bytes = bytes(f'{x}', encoding='utf-8')
    producer.send('foobar', key=key_bytes, value=value_bytes)

producer.flush()
print('done')




