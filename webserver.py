from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    message = "Discord Bot is running"
    return message

def run():
    host = "0.0.0.0"
    port = 8080
    app.run(host, port)

def keep_awake():
    thread = Thread(target=run)
    thread.start()