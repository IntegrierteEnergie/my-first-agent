# fred/agent.py
from fred.llm import chat


class FredAgent:
    """
    Der Agent-Kern. Verwaltet den Gesprächsverlauf und ruft das LLM auf.
    Später kommen hier Werkzeuge und Memory dazu.
    """

    def __init__(self):
        self.conversation_history = []  # kurzfristige Memory – erstmal nur RAM

    def chat(self, user_message: str) -> str:
        # Nachricht zur History hinzufügen
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # LLM aufrufen mit gesamter History
        response = chat(self.conversation_history)

        # Antwort auch in History speichern
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })

        return response

    def reset(self):
        """Gesprächsverlauf löschen – neuer Chat."""
        self.conversation_history = []