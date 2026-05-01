from app.vector_store import search_context

def load_business_data():
    # 🧠 MOCK BUSINESS DATA (no file dependency)
    return [
        "Free delivery in Dubai within 24 hours",
        "Cash on delivery available in UAE",
        "1 year warranty on all products",
        "24/7 customer support",
        "Office located in Dubai Marina",
        "We serve all UAE regions with fast logistics",
        "Premium AI automation services for businesses"
    ]


def get_relevant_context(user_query):
    try:
        # 🚀 FAISS VECTOR SEARCH (PRIMARY SYSTEM)
        result = search_context(user_query)

        if result and result.strip():
            return result

    except Exception:
        pass  # silently fallback

    # 🧠 SIMPLE FALLBACK (SAFE MODE)
    chunks = load_business_data()

    matches = [
        chunk for chunk in chunks
        if any(word.lower() in chunk.lower() for word in user_query.split())
    ]

    return "\n".join(matches) if matches else chunks[0]