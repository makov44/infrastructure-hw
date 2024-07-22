from fastapi import FastAPI, WebSocket, Form
from fastapi.responses import HTMLResponse
import redis
import os
import asyncio
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World Broadcasts</title>
    </head>
    <body>
        <h1>Hello World Broadcasts</h1>
        <ul id='messages'>
        </ul>
        <div id='debug'></div>       
        <script>
            var protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            var wsUrl = protocol + '//' + window.location.host + '/ws';
            var debug = document.getElementById('debug');
            debug.innerHTML += 'Attempting to connect to WebSocket at: ' + wsUrl + '<br>';
            var ws = new WebSocket(wsUrl);
            ws.onopen = function(event) {
                debug.innerHTML += 'WebSocket connection opened<br>';
            };
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            ws.onerror = function(event) {
                debug.innerHTML += 'WebSocket error observed: ' + JSON.stringify(event) + '<br>';
            };
            ws.onclose = function(event) {
                debug.innerHTML += 'WebSocket connection closed: ' + JSON.stringify(event) + '<br>';
            };
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():    
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()    
    r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)
    p = r.pubsub()
    p.subscribe('hello_channel')
    try:
        while True:
            message = p.get_message(timeout=1.0)
            if message and message['type'] == 'message':
                await websocket.send_text(f"Received: {message['data'].decode('utf-8')}")                
            await asyncio.sleep(0.1)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        p.unsubscribe('hello_channel')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")