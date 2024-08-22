# dataspheres-ai

`dataspheres-ai` is an open-source Python library for managing real-time event streams and conversations for group chats involving humans and multiple AIs. It provides seamless integration with various AI models (OpenAI, LLAMA3, Claude-3, Mistral, etc.) and offers a custom JavaScript SDK for frontend integration.

## Features

- Real-time event streaming using WebSockets
- Group chat management for humans and AI participants
- AI model agnostic integration
- Instruction tuning for configuring AI behavior

## Installation

To install `dataspheres-ai`, use:

```bash
pip install dataspheres-ai
```

## Usage

To use dataspheres-ai, import the necessary modules and create an instance of the main components:

```python
from dataspheres_ai import EventStream, ChatManager, AIManager

event_stream = EventStream()
chat_manager = ChatManager(event_stream)
ai_manager = AIManager()

# Example usage
chat_manager.create_chat('chat_1')
chat_manager.add_message('chat_1', {'user': 'Alice', 'text': 'Hello, AI!'})
ai_manager.register_ai('ai_1', {'model': 'OpenAI'})
response = ai_manager.process_message('ai_1', 'Hello, AI!')
chat_manager.add_message('chat_1', {'user': 'AI', 'text': response})
```

## License

This project is licensed under the MIT License.
