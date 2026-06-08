# 🤖 AI Document Chatbot

An AI-powered Document Chatbot built using **Streamlit**, **FAISS**, **Sentence Transformers**, and **Groq LLM**. Upload documents in multiple formats and ask questions in natural language to receive intelligent, context-aware answers.

---

## 🚀 Features

* 📄 Supports PDF, DOCX, PPTX, TXT, HTML, and Markdown files
* 📊 Supports CSV and Excel documents
* 🖼️ OCR support for images (JPG, JPEG, PNG)
* 🔍 Semantic search using FAISS vector database
* 🤖 AI-generated answers using Groq LLM
* 💬 Chat-style conversation interface
* 📚 Recent chat history management
* 📥 Download conversation history
* ⚡ Fast document retrieval with embeddings
* 🎨 Modern Streamlit user interface

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & NLP

* Groq LLM
* Sentence Transformers

### Vector Search

* FAISS

### Document Processing

* PyMuPDF
* PyPDF
* Python-Docx
* Python-PPTX
* Pandas
* BeautifulSoup
* Markdown

### OCR

* Tesseract OCR
* Pytesseract

---

## 📂 Supported File Types

| File Type | Supported |
| --------- | --------- |
| PDF       | ✅         |
| DOCX      | ✅         |
| PPTX      | ✅         |
| TXT       | ✅         |
| CSV       | ✅         |
| XLSX      | ✅         |
| JPG/JPEG  | ✅         |
| PNG       | ✅         |
| HTML      | ✅         |
| Markdown  | ✅         |

---

## 📸 Workflow

1. Upload one or more documents.
2. Text is extracted from the uploaded files.
3. Documents are split into chunks.
4. Embeddings are generated using Sentence Transformers.
5. FAISS creates a vector index.
6. User asks a question.
7. Relevant chunks are retrieved.
8. Groq LLM generates a contextual answer.

---

## 🎯 Use Cases

* Student Study Assistant
* Research Document Analysis
* Resume & Report Search
* Technical Documentation Chat
* Knowledge Base Assistant
* Educational Content Exploration

---

## 📈 Future Improvements

* Multi-document comparison
* Conversation memory across sessions
* User authentication
* Cloud storage integration
* Citation-based answers
* Advanced analytics dashboard

---

## 👨‍💻 Author

**Karthik Raja**

AI & Machine Learning Enthusiast | Full Stack Developer | Problem Solver

---

⭐ If you found this project useful, consider giving it a star.
