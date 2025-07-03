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

from tool_executor import execute_tool as run_tool
from ai_integration import AIIntegration

ai = AIIntegration()

# AI-driven orchestration endpoint
@app.route('/api/execute', methods=['POST'])
def execute_tool():
    data = request.json
    target_url = data.get("params", {}).get("target_url")
    scan_state = {"target_url": target_url, "tools_run": []}
    results = []
    last_result = None

    while True:
        action = ai.suggest_next_action(scan_state, last_result)
        if not action:
            break
        tool = action["tool"]
        params = action["params"]
        tool_result = run_tool(tool, params)
        results.append({"tool": tool, "params": params, "result": tool_result})
        scan_state["tools_run"].append(tool)
        last_result = tool_result

    analysis = ai.analyze_results(results)
    return jsonify({"status": "complete", "results": results, "ai_analysis": analysis}), 200

# WebSocket event for real-time updates
@socketio.on('connect')
def handle_connect():
    emit('status', {'message': 'Connected to HexStrike backend.'})

if __name__ == '__main__':
    eventlet.monkey_patch()
    socketio.run(app, host='0.0.0.0', port=5000)
