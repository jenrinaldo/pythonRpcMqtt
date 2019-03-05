import xmlrpc.client
import paho.mqtt.client as mqtt
import time

ip = "127.0.0.1"
port = 1883
topikSub = "/status/1"
topikSub2 = "/saldo/1"
clientRpc = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")
clientMqtt = mqtt.Client(client_id="sub1", clean_session=False)

def on_message(clientMqtt, obj, msg):
    print(msg.payload.decode("utf-8"))

clientMqtt.on_message = on_message
print("Connect to ",ip)
clientMqtt.connect(ip,port=port)
print("Subscribe to ",topikSub)
print("Subscribe to ",topikSub2)
clientMqtt.loop_start()
clientRpc.beli(10000)
clientMqtt.subscribe(topikSub,qos=2)
clientMqtt.subscribe(topikSub2,qos=2)
clientMqtt.loop_stop()
