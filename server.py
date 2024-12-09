from flask import Flask, jsonify
import time
import threading
import random

app = Flask(__name__)


JOB_DURATION = 30  # Total time for job completion, can be changed according to the requirements.
start_time = time.time()
job_status = {"result": "pending", "progress": 0}  # Initial values

# Simulate a job running 
def simulate_job():
    global job_status
    for i in range(JOB_DURATION):
        time.sleep(1)  # Increment progress every second
        job_status["progress"] = int((i + 1) / JOB_DURATION * 100)
    
    # Randomly decide if the job completes successfully or fails
    if random.random() < 0.2:  # 20% chance of failure
        job_status["result"] = "error"
    else:
        job_status["result"] = "completed"

# Start the simulation 
thread = threading.Thread(target=simulate_job)
thread.start()

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(job_status)

if __name__ == "__main__":
    app.run(port=5000)
