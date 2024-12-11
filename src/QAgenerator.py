import os
import pinecone
from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from src.prompt import *
from src.helper import download_huggingface_embeddings


load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")


# Download Embedding Model
embedding = download_huggingface_embeddings()


# Initializing Pinecone database
pinecone.Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot"

docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embedding)


# Define LLM Model
llm = ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key = NVIDIA_API_KEY,
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024
)


# Create Retrieval QA
retriever = docsearch.as_retriever(search_kwargs={"k": 2})
question_answer_chain = create_stuff_documents_chain(llm=llm, prompt=PROMPT)
qa_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=question_answer_chain)