from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'joesecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
   
if __name__ == "__main__":
    socketio.run(app, debug=True)
