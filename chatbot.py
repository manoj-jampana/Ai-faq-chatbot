from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from vector_store import create_vector_store

load_dotenv()


# Create FAISS vector store
vector_store = create_vector_store()


# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)


def ask_chatbot(question):

    # Retrieve relevant FAQs
    results = vector_store.similarity_search_with_score(
        question,
        k=2
    )

    # Keep relevant results
    relevant_results = []

    for result, score in results:
        if score < 1.0:
            relevant_results.append(result.page_content)

    # No relevant information found
    if not relevant_results:
        return "I don't have information about that."

    # Create context
    context = "\n\n".join(relevant_results)

    # Create prompt
    prompt = f"""
You are an AI FAQ assistant for a college.

Use only the information provided in the context.

Rules:
1. Do not make up information.
2. If the answer is not available in the context, say:
   "I don't have information about that."
3. Keep the answer short and easy to understand.

CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    # Generate answer
    response = llm.invoke(prompt)

    return response.text


    response = llm.invoke(prompt)

    return response.text