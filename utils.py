from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFacePipeline
from huggingface_hub import InferenceClient  
from pypdf import PdfReader
from huggingface_hub import login

# Use your Hugging Face API token to authenticate
huggingface_token = "API_KEY"  # Replace with your token
login(huggingface_token)

# Set the model ID for the hosted model
# model_id = "mistralai/Mistral-7B-v0.1"
model_id = "tiiuae/falcon-7b-instruct"
client = InferenceClient(model_id)

def process_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len
    )
    
    chunks = text_splitter.split_text(text)
    
    embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    knowledgeBase = FAISS.from_texts(chunks, embeddings)
    
    return knowledgeBase

def summarizer(pdf):
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        knowledgeBase = process_text(text)   
        # query = "Summarize the content of the uploaded PDF file in approximately 3 to 6 sentences."
        query = "Please summarize the main points of this document in about 3-5 sentences."
        if query:
            docs = knowledgeBase.similarity_search(query)
            
            # Using Hugging Face model instead of OpenAI's ChatOpenAI
            context = " ".join([doc.page_content for doc in docs])
            prompt = f"Summarize the following text:\n{context}"

            response = client.text_generation(prompt, max_new_tokens=200)
     
            return response


