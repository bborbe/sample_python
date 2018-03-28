#!/usr/bin/env python3

import time
import paho.mqtt.client as paho

broker = 'localhost'
queue = 'house/bulb1'
username = "user"
password = "pass"

client = paho.Client('client-002')
client.username_pw_set(username=username, password=password)
print('connecting to broker {}'.format(broker))
res = client.connect(broker)
if res != paho.MQTT_ERR_SUCCESS:
    print('connect failed: {}'.format(paho.error_string(res)))
    exit(1)
print('publishing to {}'.format(queue))
res = client.publish(queue, 'hello world')
if res[0] != paho.MQTT_ERR_SUCCESS:
    print('publish failed: {}'.format(paho.error_string(res)))
    exit(1)
res = client.disconnect()
if res != paho.MQTT_ERR_SUCCESS:
    print('disconnect failed: {}'.format(paho.error_string(res)))
    exit(1)
print('done')
