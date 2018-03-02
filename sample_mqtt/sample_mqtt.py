#!/usr/bin/env python3

import time
import paho.mqtt.client as paho

broker = 'localhost'
queue = 'house/bulb1'
username = "user"
password = "pass"

def on_message(client, userdata, message):
    print('received message = {}'.format(str(message.payload.decode('utf-8'))))


client = paho.Client('client-001')
client.on_message = on_message
client.username_pw_set(username=username, password=password)

print('connecting to broker {}'.format(broker))
client.connect(broker)
client.loop_start()

print('subscribing to {}'.format(queue))
client.subscribe(queue)
time.sleep(2)

print('publishing to {}'.format(queue))
client.publish(queue, 'hello world')
time.sleep(4)

print('done')
client.disconnect()
client.loop_stop()
