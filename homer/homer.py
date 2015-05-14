import pika
import time


params = pika.ConnectionParameters()
conn = pika.BlockingConnection(parameters=params)
channel = conn.channel()
channel.basic_qos(prefetch_count=1)
queue = channel.queue_declare('buffet')


try:
    for method, properties, body in channel.consume('buffet'):
        if body == 'shrimp':
            time.sleep(5)
            print("Woohoo!")
            channel.basic_ack(method.delivery_tag)
        elif body == 'kale':
            time.sleep(30)
            print("D'oh!")
            channel.basic_ack(method.delivery_tag)
finally:
    channel.cancel()
    conn.close()
