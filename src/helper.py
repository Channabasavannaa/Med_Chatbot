from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings




def LoadPDF(Data):
    loader = DirectoryLoader(Data, glob="*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()
    return docs




def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    chunks = text_splitter.split_documents(extracted_data)
    return chunks




def embedding_model():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings