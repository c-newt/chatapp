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
   
socketio.run(
    app,
    host=os.getenv('IP', '127.0.0.1'),
    port=int(os.getenv('PORT', 5001)),
    debug=True
)
