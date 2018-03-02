# MQTT

## Start MQTT server

```
echo "user:pass" > mosquitto_passwd
mosquitto_passwd -U mosquitto_passwd
```

```
docker run \
-ti \
-p 1883:1883 \
-p 9001:9001 \
-v $(pwd):/mosquitto/config \
eclipse-mosquitto
```

## Run sample

```
./sample_mqtt.py
```


mosquitto.conf:/mosquitto/config/mosquitto.conf
