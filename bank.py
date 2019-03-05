from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import paho.mqtt.client as mqtt

ip = "127.0.0.1"
mqttPort = 1883
rpcPort = 8888
topikPub = "/saldo/1"
bankStatus = ""
server = SimpleXMLRPCServer((ip,rpcPort),allow_none=True)
clientRpc = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")
clientMqtt = mqtt.Client(client_id="pub1",clean_session=False)
saldo = 100000
def beli(pulsa):
    global saldo
    if pulsa<=saldo and saldo!=0:
        saldo -=pulsa
        bankStatus = "Sisa saldo "+str(saldo)
        status = "sukses"
    else :
        bankStatus = "Sisa saldo "+str(saldo)
        status = "gagal"
    print("Connect to ",ip)
    clientMqtt.connect(ip,port=mqttPort)
    print("Publish to ",topikPub)
    clientMqtt.loop_start()
    clientMqtt.publish(topikPub,payload=bankStatus,qos=2)
    clientMqtt.loop_stop()
    clientRpc.status(status)
server.register_function(beli,"beli")
server.serve_forever()