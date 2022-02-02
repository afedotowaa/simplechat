import time
from datetime import datetime


all_messages = [{
    "text": "hello everybody",
    "name": "somebody",
    "time": time.time()
},
{
    "text": "hello my friend",
    "name": "anybody",
    "time": time.time()
}
]

def add_message(name, text):
    new_message = {
        "name": name,
        "text": text,
        "time": time.time()
    }
    all_messages.append(new_message)

add_message("n", "go sleep")

def print_message(msg):
    readable_time = datetime.fromtimestamp(msg['time'])
    print(f"{msg['name']} / {readable_time}")
    print(msg["text"])


for message in all_messages:
    print_message(message)
    print('-'*20)