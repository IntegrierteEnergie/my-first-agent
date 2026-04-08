# my-first-agent
(Remark: 8.4.2026: I will set up the videos and corresponding versions step by step, so stay tuned !)

FRED – My First Agent

Build your first AI agent step by step – from simple chat to real energy system interaction.


This repository accompanies the YouTube series “Who is FRED?” / “My First Agent”.
You will build your own AI agent for heat planning and energy systems – starting simple, but with a clean and extensible architecture.

🧠 What is FRED?

FRED is not just a chatbot.

FRED is a structured AI agent that:

understands your questions
responds via a language model
can be extended with tools, memory, and simulations

👉 The goal is not a demo – but a foundation you can build on.

🎯 What you will learn
How to structure an AI agent (UI, LLM, prompts)
How to connect a language model (API or local)
How to extend an agent step by step:
reading documents
remembering context
running simulations
orchestrating multiple models
🗺️ Course Structure (Milestones)

Each milestone corresponds to a video and a release/tag in this repository:

Milestone	Description
M1 – FRED lebt	Basic agent with Streamlit UI and LLM connection
M2 – FRED liest	Add PDF reading and first reasoning capabilities
M3 – FRED erinnert sich	Add memory (chat + vector database)
M4 – FRED rechnet	Connect to pandapipes for heat network simulation
M5 – FRED koordiniert	Multi-model orchestration

👉 Checkout a specific stage via releases/tags.

⚙️ Requirements
Python (>= 3.10 recommended)
IDE (e.g. PyCharm or VS Code)
Git
Streamlit
Access to an LLM:
via API (e.g. Qwen)
or locally (e.g. Ollama)
pandapipes (a packages connected to pandapipes)

🛠️ Setup
# Clone repository
git clone https://github.com/YOUR_USERNAME/fred-agent.git
cd fred-agent

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt (coming soon)

# Run app
streamlit run app.py
🧩 Project Structure
fred-agent/
│── app.py              # Streamlit UI + orchestration
│── llm/
│   └── client.py      # LLM API connection
│── prompts/
│   └── system_prompt.py
│── config/
│   └── settings.py

👉 Each part has a clear responsibility.
👉 This is the key to building real agents later.

💡 Philosophy

This project follows a simple principle:

Understand first. Scale later.

No heavy frameworks
No hidden magic
No copy-paste chaos

Instead:
clean structure
full control
step-by-step evolution


🚀 Where to start

👉 Start with M1 – FRED lebt 
Then move forward milestone by milestone.

🤝 Contributing / Using the Code

Feel free to:

use the code
modify it
build your own agents

This project is meant for learning, experimenting, and extending.

📄 License

MIT License – use it freely, but remember me ;)

🎓 Final Thought

If FRED runs on your machine,
you’ve taken your first real step into agentic AI.
