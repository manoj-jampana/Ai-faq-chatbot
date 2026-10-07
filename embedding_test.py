from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "What are the library timings?"

vector = embeddings.embed_query(text)

print("Number of values:", len(vector))
print("First 5 values:", vector[:5])