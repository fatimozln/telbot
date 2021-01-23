import requests
import time


token = '1428397414:AAFHMzYbyEE08RSra6DU9mj6dEtdNI67XHE'
direction = 'http://api.telegram.org/bot{}/'.format(token)

message_id = 0


def get_message():

    global message_id

    processes = requests.post(direction+"getUpdates", {"offset": message_id})
    output = processes.json()

    for i in output["result"]:

        message_id = i["update_id"]
        message_id += 1
        print(i["message"]["text"])

    print("**********")


while True:
    get_message()
    time.sleep(5)
