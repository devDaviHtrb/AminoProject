from flask import Flask 
from flask_socketio import SocketIO, emit 
app = Flask(__name__) 
socketio = SocketIO(app, cors_allowed_origins="*") 
@app.route('/') 
def index(): 
    return 'Servidor Flask rodando com ngrok!' 
if __name__ == '__main__': 
    socketio.run(app, host='0.0.0.0', port=5000) 
