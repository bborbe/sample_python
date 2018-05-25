#!/usr/bin/env python3

import time
import paho.mqtt.client as paho


def on_message(client, userdata, message):
    print('{} received message = {}'.format(message.topic, str(message.payload.decode('utf-8'))))


broker = 'localhost'
queue = 'house/bulb1'
username = "user"
password = "pass"

client = paho.Client('client-003')
client.on_message = on_message
client.username_pw_set(username=username, password=password)
print('connecting to broker {}'.format(broker))
res = client.connect(broker)
if res != paho.MQTT_ERR_SUCCESS:
    print('connect failed: {}'.format(paho.error_string(res)))
    exit(1)
res = client.loop_start()
if res == paho.MQTT_ERR_INVAL:
    print('start loop failed: {}'.format(paho.error_string(res)))
    exit(1)
print('subscribing to {}'.format(queue))
res = client.subscribe(queue)
if res[0] != paho.MQTT_ERR_SUCCESS:
    print('subscribe failed: {}'.format(paho.error_string(res)))
    exit(1)
time.sleep(60)
res = client.disconnect()
if res != paho.MQTT_ERR_SUCCESS:
    print('disconnect failed: {}'.format(paho.error_string(res)))
    exit(1)
res = client.loop_stop()
if res == paho.MQTT_ERR_INVAL:
    print('stop loop failed: {}'.format(paho.error_string(res)))
    exit(1)
print('done')
