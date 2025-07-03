import eventlet
eventlet.monkey_patch()

import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hexstrike-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Redis connection (for job queue management)
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
redis_client = redis.from_url(redis_url)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# Placeholder: Tool execution endpoint
@app.route('/api/execute', methods=['POST'])
def execute_tool():
    data = request.json
    # TODO: Implement tool execution logic
    return jsonify({"status": "pending", "data": data}), 202

# WebSocket event for real-time updates
@socketio.on('connect')
def handle_connect():
    emit('status', {'message': 'Connected to HexStrike backend.'})

if __name__ == '__main__':
    eventlet.monkey_patch()
    socketio.run(app, host='0.0.0.0', port=5000)
