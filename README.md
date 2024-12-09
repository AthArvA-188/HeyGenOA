# HeyGenOA
OA task of HeyGen


Two approaches used to solve the problem:

1. Client - Server - Integration
     This includes three files client.py, server.py and integration.py
     
  The server will return statuses like pending, completed, or error, and the client will repeatedly check the status until it either succeeds or times out.
  
  --Using the Client Library--
  
  1.1 Run the Server (Simulated)
  Run the server script first:
  python server.py
  
  1.2 For the Client side
  Once the server is running, run the integration:
  python integration.py
  
  Example Output for client side:
  (OA) PS D:\USC\OA\Heygen> python integration.py
  Status: pending, Progress: 16%
  Status: pending, Progress: 20%
  Status: pending, Progress: 26%
  Status: pending, Progress: 40%
  Status: pending, Progress: 66%
  Status: pending, Progress: 93%
  Status: completed, Progress: 100%
  Final Result: completed

2. Client-Server with SocketIO
     This includes two files 2client.py and 2server.py
   
  The server will return statuses like pending, completed, or error, and the client will disconnect after the first try. No need of integration file.
 
  --Using the Client Library--
  2.1 Run the server
    Run server script:
    python 2server.py

  2.2 Run the client script:
    python 2client.py
    

    
