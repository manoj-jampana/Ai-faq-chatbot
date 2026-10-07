from langchain_community.vectorstores import FAISS

from faq_data import faq_data
from embeddings import get_embedding_model


def create_vector_store():

    embeddings = get_embedding_model()

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

    return vector_store