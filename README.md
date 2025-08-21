# 📄 AI Research Paper Q&A

A conversational AI application built with Streamlit and LangChain that allows users to upload a research paper (PDF) and ask questions about its content.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_DEPLOYED_APP_LINK_HERE)

## 🎥 Video Demo

[Watch a 60-second demo of the app in action here!](YOUR_LOOM_VIDEO_LINK_HERE)

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