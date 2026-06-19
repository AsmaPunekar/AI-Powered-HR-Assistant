# 🤖 AI-Powered HR Assistant (RAG-Based HR Policy Chatbot)

>**Generative AI | LangChain | RAG | Large Language Models**
>**This project is part of Professional Certificate Program in Generative AI and Machine Learning - IITG by SimpliLearn Learning Platform

**Author:** **Asma I. Punekar**

---

# 📌 Project Overview

Organizations maintain extensive HR policy documents that employees frequently need to reference. Manually searching through lengthy PDF documents is time-consuming and inefficient.

This project develops an **AI-powered HR Assistant** using **Retrieval-Augmented Generation (RAG)** that answers employee questions by retrieving relevant information from HR policy documents. The chatbot combines **LangChain**, **vector embeddings**, **ChromaDB**, and **Large Language Models (LLMs)** to deliver accurate, context-aware responses.

---

# 🎯 Project Objectives

* Build an intelligent HR policy chatbot.
* Extract and process HR policy documents.
* Generate vector embeddings for efficient document retrieval.
* Implement Retrieval-Augmented Generation (RAG).
* Provide accurate, context-aware answers using an LLM.
* Design an interactive chatbot interface with Gradio.

---

# 📂 Dataset

The project uses one or more HR Policy PDF documents as the knowledge base.

The documents are:

* Loaded from PDF files
* Split into text chunks
* Converted into vector embeddings
* Stored in a vector database for semantic search

---

# 🛠️ Technologies Used

* Python
* LangChain
* Hugging Face
* ChromaDB
* Sentence Transformers
* Gradio
* PyPDFLoader
* RecursiveCharacterTextSplitter
* Large Language Models (LLMs)

---

# 🧠 Project Workflow

## 1. Document Loading

* Load HR Policy PDF documents
* Extract text using PyPDFLoader

---

## 2. Text Processing

* Split documents into smaller chunks
* Preserve semantic context
* Prepare text for embedding generation

---

## 3. Embedding Generation

Generate vector embeddings using Sentence Transformers to represent document content in vector space.

---

## 4. Vector Database

Store embeddings in **ChromaDB** for efficient similarity search and retrieval.

---

## 5. Retrieval-Augmented Generation (RAG)

The chatbot workflow:

* Receive user query
* Convert query into embeddings
* Retrieve relevant document chunks
* Pass retrieved context to the LLM
* Generate an accurate and context-aware response

---

## 6. User Interface

Developed an interactive chatbot using **Gradio**, allowing users to ask HR-related questions in natural language.

---

# 📊 Key Features

* PDF-based Question Answering
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Context-Aware Responses
* Interactive Chatbot Interface
* Enterprise HR Knowledge Assistant

---

# 📈 Results

The chatbot successfully answers HR policy questions by retrieving relevant document sections before generating responses. The RAG architecture improves response accuracy, minimizes hallucinations, and provides reliable, context-aware answers for enterprise HR use cases.

---

# ▶️ Run the Application

```bash
python app.py
```

Launch the Gradio interface in your browser and start asking questions about the HR policy documents.

---

# 📌 Future Enhancements

* Multi-document support
* Conversation memory
* Role-based HR assistant
* Streamlit deployment
* Docker containerization
* Integration with enterprise HR systems
* Support for multiple LLM providers

---

# 👩‍💻 Author

**Asma I. Punekar**

**Data Scientist | Machine Learning Engineer | Generative AI Enthusiast**

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

