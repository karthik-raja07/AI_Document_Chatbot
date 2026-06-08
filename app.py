import streamlit as st
from utils.extract_text import extract_text
from utils.chunk_text import chunk_text
from utils.embeddings import create_embeddings
from utils.vector_store import create_faiss_index
from utils.search import search_chunks
from utils.embeddings import model
from utils.groq_answer import get_answer

st.set_page_config(page_title="AI Document Chatbot",page_icon="https://img.icons8.com/?size=100&id=10446&format=png&color=000000",layout="wide")
# Session State
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = None

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "display_chat" not in st.session_state:
    st.session_state.display_chat = []
if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "index" not in st.session_state:
    st.session_state.index = None
# Sidebar
st.sidebar.title("Recent Chats")

for file_name in st.session_state.chats.keys():

    display_name = file_name.rsplit(".", 1)[0]

    if st.sidebar.button(f"📄 {display_name}"):

        st.session_state.current_chat = file_name

        st.session_state.display_chat = (
            st.session_state.chats[file_name]
        )

        st.session_state.uploaded_files = None

        st.rerun()

if st.sidebar.button("➕ New Chat"):

    st.session_state.current_chat = None
    st.session_state.uploaded_files = None
    st.session_state.chunks = None
    st.session_state.index = None
    st.session_state.display_chat = []
    st.session_state.conversation = []

    st.rerun()

if st.session_state.current_chat:

    st.sidebar.markdown("---")
    st.sidebar.write(
        f"Current: {st.session_state.current_chat.rsplit('.',1)[0]}"
    )
st.markdown("""
<div style='text-align:center;padding:20px'>
<h1>🤖 AI Document Chatbot</h1>
<h4>Ask Questions. Get Answers. Instantly.</h4>
</div>
""", unsafe_allow_html=True)
# Upload
uploaded_files = st.file_uploader(
    "Upload Document",
    type=[
        "pdf", "txt", "docx", "pptx",
        "csv", "xlsx", "jpg", "jpeg",
        "png", "html", "md"
    ],
    accept_multiple_files=True
)

if uploaded_files:
    st.session_state.uploaded_files = uploaded_files

# Clear Chat
if st.button("Clear Chat"):

    if st.session_state.current_chat:

        st.session_state.chats[
            st.session_state.current_chat
        ] = []

        st.session_state.display_chat = []

    st.rerun()

# Process Uploaded Documents
if st.session_state.uploaded_files:

    first_file_name = st.session_state.uploaded_files[0].name

    if first_file_name not in st.session_state.chats:
        st.session_state.chats[first_file_name] = []

    st.session_state.current_chat = first_file_name

    st.subheader("Uploaded Files")

    for file in st.session_state.uploaded_files:
        st.write(f"✓ {file.name}")
    text = ""
    try:

        for uploaded_file in st.session_state.uploaded_files:
            text += extract_text(uploaded_file) + "\n"

    except Exception:

        st.error(
            "❌ Unable to read the uploaded document."
        )
        st.stop()
    if st.session_state.chunks is None:
        st.session_state.chunks = chunk_text(text)

        if len(st.session_state.chunks) == 0:
            st.warning("No text extracted from document.")
            st.stop()

        with st.spinner("Processing document..."):
            try:

                embeddings = create_embeddings(
                    st.session_state.chunks
                )

                st.session_state.index = create_faiss_index(
                embeddings
                )

            except Exception:

                st.error(
                    "❌ Failed to process document."
                )
                st.stop()

    st.info("Ask a question about your document")
    query = st.text_input("Ask a Question")
    ask_button = st.button("🚀 Ask")

    if query and ask_button:

        query_embedding = model.encode(query)
        try:

            results = search_chunks(
                query_embedding,
                st.session_state.index,
                st.session_state.chunks
                )
            context = "\n".join(results)

            with st.spinner("🤖 Thinking..."):

                answer = get_answer(
                    query,
                    context,
                    st.session_state.conversation
                )
        except Exception:

            answer = (
                "❌ Sorry, I couldn't generate an answer right now. Please try again."
            )

        st.session_state.conversation.append(
            {
                "question": query,
                "answer": answer
            }
        )

        new_chat = {
            "question": query,
            "answer": answer
        }

        if (
            len(
                st.session_state.chats[
                    st.session_state.current_chat
                ]
            ) == 0
            or
            st.session_state.chats[
                st.session_state.current_chat
            ][-1]["question"] != query
        ):

            st.session_state.chats[
                st.session_state.current_chat
            ].append(new_chat)

        st.session_state.display_chat = (
            st.session_state.chats[
                st.session_state.current_chat
            ]
        )

# Conversation Display
if st.session_state.display_chat:

    st.subheader("Conversation")

    for chat in st.session_state.display_chat:

        st.markdown(
            f"**You:** {chat['question']}"
        )

        st.success(chat["answer"])

# Download Chat History
chat_text = ""

if (
    st.session_state.current_chat
    and
    st.session_state.current_chat in st.session_state.chats
):

    for chat in st.session_state.chats[
        st.session_state.current_chat
    ]:

        chat_text += (
            f"Q: {chat['question']}\n"
            f"A: {chat['answer']}\n\n"
        )

    st.download_button(
        "Download Chat History",
        chat_text,
        file_name="chat_history.txt"
    )
