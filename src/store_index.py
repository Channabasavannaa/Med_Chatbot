from src.helper import LoadPDF,text_split,embedding_model
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY



extracted_data = LoadPDF("Data/")
chunks = text_split(extracted_data)
embeddings = embedding_model()


pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "med-chatbot"


if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric  ="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1",
            
        )
    )




docsearch = PineconeVectorStore.from_documents(
    documents = chunks,
    index_name = index_name,
    embedding=embeddings
)

