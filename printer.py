#!/usr/bin/env python
import logging
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='p_logs', exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
interested = 'Interested in p!'
channel.queue_bind(exchange='p_logs',
                   queue=queue_name,
                   routing_key=interested)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):

    with open("p_log.txt", "a") as file:
        print("%r: %r \n" % (method.routing_key, body))
        file.write("%r: %r \n" % (method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
