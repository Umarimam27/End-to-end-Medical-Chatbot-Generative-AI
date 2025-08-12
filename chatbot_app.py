import streamlit as st
from medical_chatbot_model import MedicalChatbot
import base64
# --- Function to set background image ---
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# --- Function to apply custom CSS ---
def apply_custom_css():
    st.markdown("""
        <style>
        .block-container {
            backdrop-filter: blur(12px);
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 20px;
            padding: 3rem 3rem;
            margin-top: 20px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        .stTitle {
            text-align: center;
            color: #0a58ca;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0px;
        }
        .subheader-text {
            text-align: center;
            font-size: 1.3rem; /* reduced slightly */
            color: #333;
            margin-top: 10px;
            margin-bottom: 20px;
        }
        input[type="text"] {
            border-radius: 10px;
            padding: 1rem;
            border: 2px solid #0a58ca;
            background-color: #f9f9f9;
            font-size: 1.1rem;
            color: #333;
        }
        button[kind="secondaryFormSubmit"] {
            background-color: #0a58ca;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 8px;
            margin-top: 10px;
        }
        .user-bubble {
            background-color: rgba(200, 230, 255, 0.8); /* light blue for user */
            border-radius: 15px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            font-size: 1.1em;
            color: #003366;
        }
        .bot-bubble {
            background-color: rgba(255, 255, 255, 0.8); /* light white for bot */
            border-radius: 15px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            font-size: 1.1em;
            color: #333;
        }
        hr {
            border: none;
            height: 1px;
            background-color: #ccc;
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #666;
            margin-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)
# --- Set background and apply styles ---
set_bg_from_local('assets/medical.jpg')
apply_custom_css()
# --- Initialize the chatbot ---
chatbot = MedicalChatbot()

# --- Show the title first ---
st.title("Medical Chatbot 🤖")

# --- Custom subheading with corrected grammar ---
st.markdown('<div class="subheader-text">Hi, I\'m your Medical Bot. Ask me about a medical condition:</div>', unsafe_allow_html=True)

# --- Input box ---
user_input = st.text_input("Type your query here...", key="user_input")

# --- Add thin separator line ---
st.markdown("<hr>", unsafe_allow_html=True)

# --- Process user input and show response once ---
if user_input:
    with st.spinner("Thinking... 🤔"):
        response = chatbot.suggest_medicine(user_input)

    # Display the latest user message and bot response separately with color
    st.markdown(f'<div class="user-bubble">{user_input}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bot-bubble">{response}</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class="footer">
        © 2025 Medical Chatbot | Powered by Streamlit ⚡<br>
        <span style="font-weight: bold; color: #0a58ca;">Developer: Umar Imam</span>
    </div>
""", unsafe_allow_html=True)
