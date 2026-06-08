import streamlit as st
from groq import Groq
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
def get_answer(question, context, conversation):

    chat_history = ""

    for item in conversation[-5:]:

        chat_history += (
            f"Question: {item['question']}\n"
            f"Answer: {item['answer']}\n\n"
        )

    prompt = f"""
You are an AI document assistant.

Previous Conversation:
{chat_history}

Document Context:
{context}

Current Question:
{question}

Answer clearly and professionally.

Do not copy the context word-for-word.
Summarize and explain in natural language.

If the answer is not present in the document context,
say:
'I could not find this information in the uploaded document.'
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content