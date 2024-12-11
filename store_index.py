import os
import logging
import pinecone
from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone
from src.helper import load_pdf, text_split, download_huggingface_embeddings

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
print(PINECONE_API_KEY)


extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embedding = download_huggingface_embeddings()


# Initializing pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot"

logging.info("Index creating")
docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embedding=embedding, index_name=index_name)
logging.info("Index created")
