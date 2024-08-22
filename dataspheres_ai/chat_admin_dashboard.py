from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

chat_admin_app = FastAPI()

# Mount static files (CSS, JS)
chat_admin_app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

@chat_admin_app.get("/")
async def chat_admin_home(request: Request):
    return templates.TemplateResponse("chat_admin_home.html", {"request": request})

@chat_admin_app.get("/chats")
async def list_chats(request: Request):
    # Implement logic to fetch active chats
    chats = [{"id": "chat_1", "users": 2}, {"id": "chat_2", "users": 1}]
    return templates.TemplateResponse("chat_list.html", {"request": request, "chats": chats})

@chat_admin_app.get("/chat/{chat_id}")
async def view_chat(request: Request, chat_id: str):
    # Implement logic to fetch chat history and details
    chat_history = [
        {"client_id": "user1", "message": "Hello", "timestamp": "12:00:00 PM"},
        {"client_id": "ai_1", "message": "Hi there!", "timestamp": "12:00:05 PM"}
    ]
    return templates.TemplateResponse("chat_view.html", {"request": request, "chat_id": chat_id, "chat_history": chat_history})

@chat_admin_app.post("/send_message")
async def send_message(chat_id: str, message: str):
    # Implement logic to send a message to a specific chat
    # This could involve calling your existing chat manager or creating a new WebSocket connection
    return {"status": "Message sent"}

@chat_admin_app.get("/ai_config")
async def ai_config(request: Request):
    # Implement logic to fetch and display AI configurations
    ai_configs = [{"id": "ai_1", "model": "OpenAI"}, {"id": "ai_2", "model": "Claude"}]
    return templates.TemplateResponse("ai_config.html", {"request": request, "ai_configs": ai_configs})