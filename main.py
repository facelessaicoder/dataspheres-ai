import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from dataspheres_ai.event_stream import EventStream, ConnectionManager
from dataspheres_ai.chat_manager import ChatManager
from dataspheres_ai.ai_manager import AIManager
from dataspheres_ai.chat_admin_dashboard import chat_admin_app
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("dataspheres-ai")

app = FastAPI()

connection_manager = ConnectionManager()
event_stream = EventStream(connection_manager)
chat_manager = ChatManager(event_stream)
ai_manager = AIManager()

# Example AI registration
ai_manager.register_ai('ai_1', {'model': 'OpenAI'})

# Mount the chat admin dashboard
app.mount("/chat-admin", chat_admin_app)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await connection_manager.connect(websocket)
    logger.info(f"Client {client_id} connected")
    try:
        while True:
            try:
                data = await websocket.receive_text()
                parsed_data = json.loads(data)
                if parsed_data.get('type') == 'ping':
                    await websocket.send_json({'type': 'pong'})
                    continue
                chat_id = parsed_data.get("chat_id")
                message = parsed_data.get("message")
                logger.debug(f"Received message from {client_id}: {message}")
                if chat_id and message:
                    message_data = {
                        "client_id": client_id,
                        "message": message,
                        "timestamp": datetime.now().strftime('%I:%M:%S %p'),
                        "type": "user"
                    }
                    chat_manager.add_message(chat_id, message_data)
                    await connection_manager.broadcast(json.dumps(message_data))
                    logger.debug(f"Message added to chat {chat_id} and broadcasted")

                    # Process the message with the AI
                    ai_response = ai_manager.process_message('ai_1', message)
                    if ai_response:
                        chat_manager.add_message(chat_id, ai_response)
                        await connection_manager.broadcast(json.dumps(ai_response))
                        logger.debug(f"AI response added to chat {chat_id} and broadcasted")
                else:
                    await websocket.send_json({"error": "Invalid payload format"})
            except json.JSONDecodeError:
                logger.error("Invalid JSON format")
                await websocket.send_json({"error": "Invalid JSON format"})
    except WebSocketDisconnect as e:
        logger.info(f"Client {client_id} disconnected: {e}")
        connection_manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
