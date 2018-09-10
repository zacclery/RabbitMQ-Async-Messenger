#!/usr/bin/env python
import random
import pika
import time
import asyncio
from time_server import TimeServer

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # local for testing
channel = connection.channel()
ts = TimeServer()
channel.exchange_declare(exchange='p_logs', exchange_type='direct')

interested = 'Interested in p!'
p = 0
full_day = 24*60*60 # seconds

async def wait():
    r_in_seconds = ts.convert_to_virtual_time(0.01)*24*60*60
    await asyncio.sleep(r_in_seconds)
    print("Waited 0.01 virtual days")
    message = "I was triggered after waiting 0.01 virtual days from last print"
    channel.basic_publish(exchange='p_logs', routing_key=interested, body=message)

while True:
    r = random.uniform(0.00, 0.02)
    r_in_seconds = ts.convert_to_virtual_time(r)*24*60*60
    time.sleep(r_in_seconds)
    print("Waiting %r virtual days" % (r_in_seconds / full_day))
    s = random.uniform(0.00, 1)
    p += s
    virtual_time = ts.get_time_remaining()
    channel.basic_publish(exchange='p_logs', routing_key=interested, body=str(virtual_time))
    channel.basic_publish(exchange='p_logs', routing_key=interested, body=str(p))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait())
