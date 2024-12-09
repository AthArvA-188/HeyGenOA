from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import time
import threading
import random

app = Flask(__name__)
socketio = SocketIO(app)

JOB_DURATION = 10  # Duration in seconds
job_status = {"result": "pending", "progress": 0}
job_thread = None  # Global variable to hold the job thread

def simulate_job():
    global job_status
    failure_chance = random.random()  # Generate a random number between 0 and 1
    
    for i in range(1, 11):  # Simulating progress in 10 steps
        time.sleep(JOB_DURATION / 10)
        job_status["progress"] = i * 10  # Update progress percentage
        print(f"Emitting progress: {job_status['progress']}%") 
        socketio.emit('progress', {"progress": job_status["progress"]})
        
        # Randomly fail at 50% progress with a 30% chance
        if i == 5 and failure_chance < 0.3:  
            job_status["result"] = "error"
            socketio.emit('progress', {"progress": job_status["progress"], "result": "error"})
            print("Job failed! Emitting error status.")
            return
    
    # If no failure occurs, show completion
    job_status["result"] = "completed"
    socketio.emit('progress', {"progress": 100, "result": "completed"})
    print("Job completed successfully!")

@socketio.on('connect')
def handle_connect():
    global job_thread
    print("Client connected!")
    if job_thread is None or not job_thread.is_alive():
        job_thread = threading.Thread(target=simulate_job)
        job_thread.start()

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected!")

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(job_status)

if __name__ == "__main__":
    socketio.run(app, port=5001, debug=True) 
