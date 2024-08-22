import asyncio
import websockets
import json
from datetime import datetime

async def send_message(uri, chat_id, message):
    try:
        async with websockets.connect(uri) as websocket:
            timestamp = datetime.now().strftime('%I:%M:%S %p')
            payload = {
                "chat_id": chat_id,
                "message": message,
                "client_id": "console",
                "timestamp": timestamp
            }
            await websocket.send(json.dumps(payload))
            print(f"Sent: {json.dumps(payload)}")

            response = await websocket.recv()
            print(f"Received: {response}")

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    uri = "ws://127.0.0.1:8000/ws/console-client"
    chat_id = "chat_1"
    message = "Hello from the console!"

    asyncio.get_event_loop().run_until_complete(send_message(uri, chat_id, message))
