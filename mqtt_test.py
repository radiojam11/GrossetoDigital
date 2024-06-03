import paho.mqtt.client as mqtt
import json
import telepot
import time
import datetime
import my_API

token = my_API.API
bot = telepot.Bot(token)
topic = "dmr/bmlh/#"
mqtt_server = "mqtt.iz3mez.it"
porta = 1883
nominativo = 0


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global nominativo
    mess_BM = str(msg.payload.decode("utf-8"))
    dictionary = json.loads(mess_BM)
    if "222550" in str(dictionary["DestinationID"]):
        new_nom = dictionary['SourceID']
        #print(new_nom)
        #print(nominativo)

        # per evitare di inviare doppi messaggi, se il nominativo di questo pacchetto
        # è uguale al nominativo del messaggio precedente, non lo pubblico
        if new_nom != nominativo:
            timestamp = dictionary['Stop']
            # per evitare i messaggi ripresi vecchi, passa solo il messaggio che è 
            # al massimo più vecchio di 60 secondi, altrimenti non lo pubblico
            now = datetime.datetime.now()
            adesso = now.timestamp()
            if (adesso - timestamp ) > 60 :
                pass
            else:
                data = datetime.datetime.fromtimestamp(timestamp)
                tempo = dictionary['Stop'] - dictionary['Start']
                ber = round(dictionary['BER'] * 100, 2)
                if ber < 0 :
                    ber = 0
                if len(dictionary['DestinationCall']) == 0 :
                    dictionary['DestinationCall'] = "Grosseto Talk"
                stringa = "Call: {}  User ID: {}\nTS: {}  TG: {} ✴️ {}\nRpt: {} [{}-{}]\nTalker Alias: {}\nRSSI: {}dBm  BER: {}%\nFine TX: {}\nDuration: {}s 🔊".format( dictionary['SourceCall'], dictionary['SourceID'], dictionary['Slot'], dictionary['DestinationID'], dictionary['DestinationCall'] ,dictionary['LinkCall'],dictionary['Master'],dictionary['ContextID'], dictionary['TalkerAlias'], dictionary['RSSI'], ber, data, tempo)
                inviato = bot.sendMessage(-1002212992476, stringa) 
                nominativo = new_nom
                print(stringa)
        else:
            nominativo = 0


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(mqtt_server, porta, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()

