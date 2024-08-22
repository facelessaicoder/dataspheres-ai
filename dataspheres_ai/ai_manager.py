from datetime import datetime

class AIManager:
    def __init__(self):
        self.ais = {}

    def register_ai(self, ai_id, ai_config):
        """
        Registers an AI with the given configuration.
        :param ai_id: Unique identifier for the AI.
        :param ai_config: Configuration dictionary for the AI.
        """
        self.ais[ai_id] = ai_config

    def get_ai_config(self, ai_id):
        """
        Retrieves the configuration for a given AI.
        :param ai_id: Unique identifier for the AI.
        :return: Configuration dictionary for the AI or None if not found.
        """
        return self.ais.get(ai_id)

    def process_message(self, ai_id, message):
        """
        Processes a message using the specified AI.
        :param ai_id: Unique identifier for the AI.
        :param message: The message to be processed by the AI.
        :return: The AI's response to the message.
        """
        ai_config = self.get_ai_config(ai_id)
        if ai_config:
            # This is where integration with the actual AI model would happen
            # For example, you could use OpenAI, LLAMA3, Claude-3, etc.
            response = f"AI ({ai_id}) response to: {message}"
            return {
                "client_id": ai_id,
                "message": response,
                "type": "ai",
                "timestamp": datetime.now().strftime('%I:%M:%S %p')
            }
        return None
