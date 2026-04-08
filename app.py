# app.py
import streamlit as st
from fred import FredAgent

# ── Seitenconfig ──────────────────────────────────────────
st.set_page_config(
    page_title="FRED – Wärmeplanung Assistent",
    page_icon="🔥",
    layout="centered"
)

# ── Session State initialisieren ──────────────────────────
if "agent" not in st.session_state:
    st.session_state.agent = FredAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Header ────────────────────────────────────────────────
st.title("🔥 FRED")
st.caption("Forschungs-Ressourcen-Energie-Dialogs-Assistent | Wärmeplanung")
st.divider()

# ── Chatverlauf anzeigen ──────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Eingabe ───────────────────────────────────────────────
if prompt := st.chat_input("Frag FRED etwas zur Wärmeplanung..."):
    # Nutzernachricht anzeigen
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # FRED denkt nach
    with st.chat_message("assistant"):
        with st.spinner("FRED denkt..."):
            response = st.session_state.agent.chat(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ FRED Status")
    st.info("Modell: qwen2.5:7b-instruct")
    st.info("Memory: aktiv (Session)")

    if st.button("🗑️ Gespräch zurücksetzen"):
        st.session_state.agent.reset()
        st.session_state.messages = []
        st.rerun()
