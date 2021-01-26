import requests
import time


token = '1428397414:AAFHMzYbyEE08RSra6DU9mj6dEtdNI67XHE'
endpoint = 'https://api.telegram.org/bot{}/'.format(token)

message_id = 0


def add(n):
    f = open("links.txt", "a")
    f.write("{}\n".format(n))
    f.close()


def get_message():
    global message_id
    output = []

    res = requests.post(endpoint+"getUpdates", {
        "offset": message_id
    })
    resp = res.json()

    for i in resp["result"]:
        message_id = i["update_id"]
        message_id += 1
        output.append(i["message"]["text"])

    return output


while True:
    for i in get_message():
        if i != "None":
            add(i)
    time.sleep(3)
