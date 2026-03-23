# 📄 AI Research Paper Q&A

A conversational AI application built with Streamlit and LangChain that allows users to upload a research paper (PDF) and ask questions about its content.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://atlan-ai-project-1.onrender.com)

## 🎥 Video Demo

[Watch a 60-second demo of the app in action here!](https://www.loom.com/share/e0c406f4646f42d09a45fb49b377c701?sid=2bc3c4b6-0cd4-4982-8ddf-f20df833135d)

## ✨ Key Features

* **Dynamic PDF Upload:** Upload any research paper PDF via a user-friendly interface.
* **Conversational Interface:** Ask questions in natural language and receive context-aware answers.
* **RAG Pipeline:** Utilizes a Retrieval-Augmented Generation (RAG) architecture to ensure answers are based on the document's content.
* **Source Verification:** Displays the exact text chunks from the document that were used to generate the answer, providing transparency.

## 🛠️ Tech Stack

* **Backend:** Python, LangChain
* **Frontend:** Streamlit
* **LLM:** Google Gemini 1.5 Flash
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Vector Store:** FAISS

## 🚀 How to Run Locally

1.  Clone the repository: `git clone [your-repo-link]`
2.  Create and activate a virtual environment.
3.  Install the dependencies: `pip install -r requirements.txt`
4.  Create a `.env` file and add your `GOOGLE_API_KEY`.
5.  Run the Streamlit app: `streamlit run app.py`

## 🚀 Problem

Understanding and extracting insights from research papers is time-consuming and inefficient. Users often struggle to find precise answers within long documents, especially when relying on traditional keyword-based search methods.

This creates a need for a system that can:
- Understand user queries contextually  
- Retrieve the most relevant information from documents  
- Generate accurate, human-like responses grounded in source content  

---

## 💡 Approach

This project implements a Retrieval-Augmented Generation (RAG) pipeline to enable intelligent document querying:

- Research papers are first processed and split into smaller chunks  
- Each chunk is converted into vector embeddings using Sentence Transformers  
- Embeddings are stored in a FAISS vector database for efficient similarity search  
- For a given user query, top relevant chunks are retrieved  
- Google Gemini API is used to generate responses based on the retrieved context  

This ensures that answers are both context-aware and grounded in actual document data  

---

## 🔁 Iterations

- Started with basic document parsing and keyword-based retrieval  
- Improved retrieval using semantic embeddings instead of keyword matching  
- Integrated FAISS to handle efficient and scalable similarity search  
- Added LLM (Gemini) to generate contextual answers instead of returning raw text  
- Continuously refined chunking strategy and retrieval parameters for better accuracy  

---

## ⚙️ Key Design Choices

- Chose RAG architecture over fine-tuning for flexibility and scalability  
- Used FAISS for fast and efficient vector similarity search  
- Implemented chunk-based retrieval to improve relevance of results  
- Integrated Gemini API for high-quality natural language responses  
- Focused on modular pipeline design for easy extension and improvements  

---

## ⏱️ Daily Time Commitment

Approximately 3–4 hours per day  

Time was primarily spent on:
- Experimenting with embeddings and retrieval techniques  
- Improving response quality and grounding  
- Debugging pipeline integration (FAISS + LLM)  
- Enhancing overall system performance and usability
