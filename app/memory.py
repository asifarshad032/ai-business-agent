# 🧠 Simple in-memory storage (NO DATABASE, NO COST)

memory_store = {}

def save_memory(user_id: str, message: str, response: str):
    """
    Save ONLY clean conversation history
    """
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append({
        "user": message,
        "ai": response
    })

    # 🔥 limit memory size (avoid infinite growth)
    if len(memory_store[user_id]) > 10:
        memory_store[user_id] = memory_store[user_id][-10:]


def get_memory(user_id: str):
    """
    Get previous conversations
    """
    return memory_store.get(user_id, [])