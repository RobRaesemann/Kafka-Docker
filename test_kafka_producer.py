from kafka import KafkaProducer
import numpy as np
import random
import asyncio
import json
import uuid
from datetime import datetime
import time

assets = ['asset1', 'asset2', 'asset3']
readings = ['reading1','reading2']
#producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))

def kafka_error(err):
    print(err)

def send(producer, payload):
        """ Send the payload, using provided producer """

        producer.send('readings'.encode('utf-8'), value=payload).add_errback(kafka_error)
        producer.flush()        


def send_payloads(payload_block):
        """ send a list of block payloads"""

        try:
            producer = KafkaProducer(bootstrap_servers=['kafkaserver:9092'], 
                api_version=(0, 11),
                value_serializer=lambda x: json.dumps(x).encode('utf-8'))

            send(producer, payload_block)
        except Exception as ex:
            print(f'Exception sending payloads: {ex}')



def _create_readings():
    
    
    payload_block = list()
    
    for asset in assets:
           
        read = dict()
        np.random.seed(int(time.time()))
        rand_readings = np.random.random(size=2)

        read['asset'] = asset
        read['readings'] =  {
                'reading1' : rand_readings[0],
                'reading2' : rand_readings[1]
            }
        read["timestamp"] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        read["key"] = str(uuid.uuid4())
        payload_block.append(read)

    return payload_block

while True:
    print('.')
    payload = _create_readings()    
    send_payloads(payload)
    time.sleep(1)

