import socketio

class VideoTranslationClient:
    def __init__(self, base_url):
        self.sio = socketio.Client(reconnection=False)  # Disable reconnection attempts (Good for use so never goes into infinite loop)
        self.base_url = base_url
        self.progress = 0
        self.result = None

    def connect(self):
        print(f"Connecting to {self.base_url}...")
        self.sio.connect(self.base_url, transports=['websocket']) 
        self.sio.on("progress", self.on_progress)  # Listen for progress events
        print("Connection established successfully")

    def on_progress(self, data):
        print(f"Received progress event: {data}")
        self.progress = data.get("progress", 0)
        print(f"Progress: {self.progress}%")
        if "result" in data and data["result"] is not None:
            self.result = data["result"]
            print(f"Final Result: {self.result}")
            self.sio.disconnect()  # Disconnect once the job is done

    def wait_for_completion(self):
        print("Waiting for job completion...")
        self.sio.wait()  # Wait for progress updates

if __name__ == "__main__":
    client = VideoTranslationClient("http://127.0.0.1:5001")
    client.connect()  # Establish connection to server
    client.wait_for_completion()  # Wait for events to be processed
