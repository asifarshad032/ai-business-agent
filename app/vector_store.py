import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# 🧠 Local embedding model (NO COST, NO API)
model = SentenceTransformer("all-MiniLM-L6-v2")

# 📦 Business Knowledge Base (Dubai style data)
documents = [
    "We deliver in Dubai within 24 hours",
    "Cash on delivery is available in UAE",
    "We provide 1 year warranty on all products",
    "Customer support is available 24/7",
    "Our office is located in Dubai Marina",
    "Free return within 7 days",
    "We support WhatsApp ordering in UAE",
    "Premium AI automation services in Dubai"
]

# 🔥 Step 1: Convert text → vectors
embeddings = model.encode(documents)

dimension = embeddings.shape[1]

# 🔥 Step 2: FAISS index (REAL vector DB)
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# 🧠 Step 3: Search function (REAL semantic search)
def search_context(query, top_k=3):
    query_vector = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = [documents[i] for i in indices[0]]

    return "\n".join(results)