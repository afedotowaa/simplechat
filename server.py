from flask import Flask, request, render_template
import time
from datetime import datetime
import json

app = Flask(__name__)

messages_file = "./data/messages.json"  # путь к файлу с сообщениями
json_file = open(messages_file, "rb")  # читаем бинарный файл
data = json.load(json_file)
if not "all_messages" in data:
    print(f"Can't find all_messages in {messages_file}")
    exit(1)

all_messages = data["all_messages"]  # загружаем json-данные и берем список "all_messages"

def save_messages():
    data = {  # создаем структуру
        "all_messages": all_messages
    }
    json_file = open(messages_file, "w")  # открываем файл для записи
    json.dump(data, json_file)  # пишем структуру в файл

def time_format(t):
    return str(datetime.fromtimestamp(t))


# ToDO сохранять сообщения в файл
# all_messages = [ # В этом списке хранятся все сообщения чата
#     { # каждое сообщение это словарь с полями text, name и time
#         "text": 'Привет всем в чате',
#         "name": "Mike",
#         "time": time_format(time.time() - 3600) # типа майк написал сообщение час (3600 сек) назад
#     },
# ]


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/")
def root():
    return "Hello everyone"


# POST — запрос на изменение данных
@app.route("/send")
def send_message():
    text = request.args["text"]
    name = request.args["name"]

    # Проверить что имя не очень длинное
    if len(name) > 100 or len(name) < 3:
        return "ERROR"

    if len(text) < 1 or len(text) > 3000:
        return "ERROR"

    message = {
        "text": text,
        "name": name,
        "time": time_format(time.time()),
    }

    all_messages.append(message)
    save_messages()

    return "OK"


app.run(host="0.0.0.0", port=80)
# 0.0.0.0 = сервер будет доступен на всех IP адресах данного компьютера
