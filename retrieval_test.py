from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from faq_data import faq_data


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


documents = []

for faq in faq_data:
    for question in faq["questions"]:
        documents.append(
            f"Question: {question}\nAnswer: {faq['answer']}"
        )


vector_store = FAISS.from_texts(
    documents,
    embeddings
)


question = "How much attendance do I need?"

results = vector_store.similarity_search(question, k=2)


print("\nRelevant FAQs:\n")

for result in results:
    print(result.page_content)
    print("--------------------")