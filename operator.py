from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import paho.mqtt.client as mqtt

ip = "127.0.0.1"
mqttPort = 1883
rpcPort = 8889
topikPub = "/status/1"
opStatus = ""
server = SimpleXMLRPCServer((ip,rpcPort), allow_none=True)
clientMqtt = mqtt.Client(client_id="pub1",clean_session=False)
def status(pulsa):
    if pulsa=="sukses":
        opStatus = "Transaksi berhasil"
    else :
        opStatus = "Transaksi gagal"
    print("Connect to ",ip)
    clientMqtt.connect(ip,port=mqttPort)
    print("Publish to ",topikPub)
    clientMqtt.loop_start()
    clientMqtt.publish(topikPub,payload=opStatus,qos=2)
    clientMqtt.loop_stop()
server.register_function(status,"status")
server.serve_forever()