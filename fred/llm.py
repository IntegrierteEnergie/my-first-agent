# fred/llm.py
import requests
import json
from config import OLLAMA_BASE_URL, MODEL_NAME, FRED_SYSTEM_PROMPT


def chat(messages: list[dict]) -> str:
    """
    Sendet eine Nachrichtenliste an Ollama und gibt die Antwort zurück.
    messages = [{"role": "user", "content": "..."}, ...]
    """
    url = f"{OLLAMA_BASE_URL}/api/chat"

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "system", "content": FRED_SYSTEM_PROMPT}] + messages,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"]