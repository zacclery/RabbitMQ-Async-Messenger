#!/usr/bin/env python
'''
Script to ping signals at printer after r seconds:
python alert_server.py 0.0001
'''
import pika
import sys
from time_server import TimeServer


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # local for testing
channel = connection.channel()
ts = TimeServer()
channel.exchange_declare(exchange='p_logs', exchange_type='direct')

interested = 'Interested in p!'
r = float(sys.argv[1]) # Pass wait time until signal. NOT OPTIONAL

r_in_seconds = ts.convert_to_virtual_time(r)*24*60*60
time.sleep(r_in_seconds)
message = "I am a signal. I waited %r virtual seconds" % r_in_seconds
channel.basic_publish(exchange='p_logs', routing_key=interested, body=message)
