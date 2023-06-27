print("MQTT with Adafruit IO")
import time
import random
import sys
import requests

from Adafruit_IO import MQTTClient

AIO_FEED_ID = "button1"
AIO_USERNAME = "hejmanh"
AIO_KEY = ""

global_equation = "x1 + x2 + x3"
def connected(client):
    print("Server connected ...")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe!! ...")
def disconnected(client):
    print("Disconnect from server ...")
    sys.exit (1)
def message(client , feed_id , payload):
    print("Received: " + payload)
    if (feed_id == "equation"):
        global_equation = payload
        print(global_equation)

def init_global_equation():
    global global_equation
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/hejmanh/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)

def modify_value(x1, x2, x3):
    result = eval(global_equation)
    print(result)
    return result

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    s1 = random.randint(20, 70)
    s2 = random.randint(0, 100)
    s3 = random.randint(0, 14)
    client.publish("sensor1", s1)
    client.publish("sensor2", s2)
    client.publish("sensor3", s3)
    s4 = modify_value(s1, s2, s3)
    print(s4)
    pass