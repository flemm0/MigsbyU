import json
import threading
from kafka import KafkaConsumer

def consume_topic(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['kafka:9092'],
        value_deserializer=lambda m: json.loads(m.decode('ascii')),
        auto_offset_reset='earliest',
        enable_auto_commit=False
    )
    for message in consumer:
        print(json.loads(message.value))

def main():
    topics = [
        'migsbyu.public.students',
        'migsbyu.public.professors',
        'migsbyu.public.courses',
        'migsbyu.public.takes',
        'migsbyu.public.teaches'
    ]

    threads = []
    for topic in topics:
        thread = threading.Thread(target=consume_topic, args=(topic,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    print('Start consuming...')
    main()