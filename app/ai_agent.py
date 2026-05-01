from app.rag import get_relevant_context
from app.memory import save_memory, get_memory

def chat_with_ai(user_message, user_id="default_user"):
    try:
        # 📦 RAG context
        context = get_relevant_context(user_message)

        # 🧠 Get memory (last 3 chats only)
        history = get_memory(user_id)

        history_text = ""
        for h in history[-3:]:
            history_text += f"User: {h['user']}\nAI: {h['ai']}\n\n"

        # 🤖 MOCK RESPONSE
        response = f"""
🤖 AI BUSINESS AGENT (MOCK MODE)

👤 User ID: {user_id}

💬 Current Message:
{user_message}

🧠 Memory (Last Conversations):
{history_text if history_text else "No previous memory"}

📦 Business Context:
{context}

💡 System Status:
- Mock Mode Active
- Memory System Active
- RAG System Active
"""

        # 🧠 FIX: store ONLY clean data (no full response)
        save_memory(user_id, user_message, "AI responded")

        return response

    except Exception as e:
        return f"ERROR: {str(e)}"