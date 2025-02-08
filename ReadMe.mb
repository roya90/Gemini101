# Gemini Flash Chatbot with Streamlit

This project is a simple chatbot application built using **Streamlit** and **Google Generative AI (Gemini Flash)**. It allows users to interact with a chatbot that answers questions about a fictional company, **Cymbal Direct**. The chatbot is powered by Google's Gemini Flash language model.

## Features
- Conversational UI built with Streamlit.
- Utilizes the Google Generative AI (Gemini Flash) API to generate responses.
- Simulates a personalized knowledge base for the company Cymbal Direct.

---

## Prerequisites
Before you begin, ensure you have the following installed:
1. Python 3.8 or higher
2. Streamlit
3. Google Generative AI SDK (`google-genai`)

---

## Installation
1. Clone this repository or copy the code into a Python file (e.g., `Cymbal.py`).
2. Install the required dependencies:
   ```bash
   pip install streamlit google-genai
   ```
3. Authenticate your Google Generative 
---

## Running the Application
1. Save the script as `Cymbal.py`.
2. Run the Streamlit application with the following command:
   ```bash
   streamlit run Cymbal.py
   ```
3. The Cymbal will launch in your default web browser.

---

## Code Overview
### Import Libraries
```python
import streamlit as st
from google import genai
from google.genai import types
```
- **Streamlit** is used for building the web-based UI.
- **Google GenAI** is used to access the Gemini Flash model.

### Generating Responses
The `generate_response` function sends user input to the Gemini Flash model and retrieves the response.
```python
def generate_response(user_input):
    client = genai.Client(vertexai=True, project="opensource-406515", location="us-central1")
    ...
    response_text = ""
    for chunk in client.models.generate_content_stream(...):
        response_text += chunk.text
    return response_text
```

### Displaying Chat History
The chat history is maintained using `st.session_state` to preserve the conversation between user and assistant.
```python
if "messages" not in st.session_state:
    st.session_state["messages"] = []
```

### User Input and Response
The application takes user input, generates a response using the `generate_response` function, and displays both in a chat format.
```python
user_input = st.text_input("You:", "")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    bot_reply = generate_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
```

---

## Customization
You can customize the chatbot by:
- Changing the **system instruction** to modify the chatbot's personality.
- Adjusting **temperature** and **top_p** in the `GenerateContentConfig` for different response styles.

---

## Conclusion
This project demonstrates how to integrate Google Generative AI with Streamlit to build an interactive chatbot. You can expand this example to create more complex applications by fine-tuning the system instructions or connecting it to external data sources.

---

## License
This project is for educational purposes. Modify and use it as needed!

