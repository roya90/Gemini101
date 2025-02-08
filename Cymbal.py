import streamlit as st
from google import genai
from google.genai import types
import base64

# Configure Streamlit UI
st.title("Gemini Flash Chatbot")
st.write("Ask me anything about Cymbal Direct!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def generate_response(user_input):
    client = genai.Client(
        vertexai=True,
        project="opensource-406515",
        location="us-central1",
    )
    
    textsi_1 = """Cymbal Direct is an online direct-to-consumer footwear and apparel retailer headquartered in Chicago. 
    
    Founded in 2008, Cymbal Direct (originally 'Antern') is a fair trade and B Corp certified sustainability-focused company that works with cotton farmers to reinvest in their communities. 
    The price range for Cymbal clothes is typically between $50 and $300.
    
    In 2010, as Cymbal Group began focusing on digitally-savvy businesses that appealed to a younger demographic of shoppers, the holding company acquired Antern and renamed it Cymbal Direct. In 2019, Cymbal Direct reported an annual revenue of $7 million and employed a total of 32 employees. 
    
    Cymbal Direct is a digitally native retailer. 
    
    You are a personalized wiki of the company Cymbal."""

    contents = [types.Content(role="user", parts=[types.Part.from_text(text=user_input)])]
    
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        top_p=0.8,
        max_output_tokens=1024,
        response_modalities=["TEXT"],
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
        system_instruction=[types.Part.from_text(text=textsi_1)],
    )
    
    response_text = ""
    for chunk in client.models.generate_content_stream(
        model="gemini-2.0-flash-001",
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text
    
    return response_text

# User input
user_input = st.text_input("You:", "")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    bot_reply = generate_response(user_input)
    
    with st.chat_message("assistant"):
        st.write(bot_reply)
    
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
