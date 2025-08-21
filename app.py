import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
import tempfile

# ----- Page Setup -----
st.set_page_config(page_title="Chat with Your PDF", page_icon="📄")
st.title("📄Chat with Your Research Papers")
st.write("Uplaod a research paper and ask it any question you have.")

# ----- loading API key -----
# this line loads the environment variables from .env file
load_dotenv()
# note: the google API key is loaded automatically by the langchain library, as long as the .env file is setup correctly.

# ----- side bar for file upload -----
with st.sidebar:
    st.header("Upload Your PDF")
    uploaded_file = st.file_uploader("Chose a PDF file", type="pdf")

# ----- function to process pdf -----
def process_pdf(pdf_path):
    # loading the pdf, splitting it into chunks, creating embeddings & storing them in a vector store.
    # 1. loading the document
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    # grabbing the first page's text
    first_page_text = documents[0].page_content

    # 2. splitting the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(documents)

    # 3. creating embeddings for the chunks
    # using a powerful open-source model that runs on local machine
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # 4. creating the vector store
    # this will download the embedding model the first time it's run.
    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store, first_page_text

# ----- Main Application Logic -----

# using session_state to store the processed data so it's not lost on rerun
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'first_page_text' not in st.session_state:
    st.session_state.first_page_text = None

if uploaded_file is not None:
    with st.spinner("Processing the PDF... This may take a moment."):
        # creating a temporary file to store the uploaded content
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        # processing the pdf & storing the result in session state
        st.session_state.vector_store, st.session_state.first_page_text = process_pdf(tmp_file_path)

        # cleaning up the temporary file
        os.remove(tmp_file_path)
        st.success("PDF has been processed successfully! You can now ask questions.")

# only showing the chat interface if a PDF has been processed 
if st.session_state.vector_store is not None:
    # creating the llm & retriever
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
    retriever=st.session_state.vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 3})

    # ----- user interface for chat -----
    st.header("Ask a Question")
    user_question = st.text_input("What do you want to know from the paper?")

    if user_question:
        with st.spinner("Finding the answer..."):
            try:
                # getting an answer
                # 1. retrieving relevant documents from the vector store
                retrieved_docs = retriever.get_relevant_documents(user_question)

                # 2. manually adding the first page to the context
                # ensuring that the title and abstract are always available
                context_docs = [retrieved_docs[0]]
                context_docs[0].page_content = st.session_state.first_page_text + "\n\n" + retrieved_docs[0].page_content

                # 3. running the question-answering chain
                chain = load_qa_chain(llm, chain_type="stuff")
                response = chain.run(input_documents=context_docs, question=user_question)

                st.write("### Answer")
                st.write(response)

                # ----- displaying the sources used -----
                with st.expander("Show Sources Used"):
                    st.write("Sources:")
                    # displaying the first page & the other retrieved docs
                    st.info(f"Source 1 (First Page):\n\n{st.session_state.first_page_text[:300]}...")
                    for i, doc in enumerate(retrieved_docs):
                        st.info(f"Source {i+2} (Retrieved chunk):\n\n{doc.page_content[:250]}...")


            except Exception as e:
                st.error(f"An error occurred: {e}")
