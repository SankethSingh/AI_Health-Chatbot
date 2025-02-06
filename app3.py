import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key1 = os.getenv("API_KEY")
if not api_key1:
    raise ValueError("API_KEY is not set in the .env file")
# Configure Gemini API
genai.configure(api_key=api_key1)  # Replace with your Gemini API key

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

# Custom CSS for UI enhancement
st.markdown("""
    <style>
    .stTextInput input {
        font-size: 18px;
        padding: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .critical-warning {
        background-color: #ffcccc;
        color: red;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# List of critical keywords to detect emergencies
CRITICAL_KEYWORDS = [
    "chest pain", "difficulty breathing", "severe bleeding",
    "unconscious", "stroke", "heart attack"
]

# Healthcare chatbot logic
def healthcare_chatbot(user_input):
    # Check if the query relates to critical cases
    is_critical = any(keyword in user_input.lower() for keyword in CRITICAL_KEYWORDS)
    
    # Handle symptom-related queries for critical cases without a warning
    if is_critical and "symptom" in user_input.lower():
        return f"The symptoms of {', '.join([kw for kw in CRITICAL_KEYWORDS if kw in user_input.lower()])} may include severe discomfort, pain, or other alarming signs. Please consult a doctor immediately.", False
    
    # Handle treatment or assistance queries for critical cases with a warning
    if is_critical and ("treat" in user_input.lower() or "assistance" in user_input.lower()):
        basic_care = (
            "For basic care:\n"
            "- Ensure the person is in a safe position.\n"
            "- Call emergency services immediately.\n"
            "- Monitor their condition until help arrives."
        )
        return f"{basic_care}\n\nCRITICAL ALERT: This appears to be a medical emergency. Immediate professional medical assistance is required.", True
    
    # Predefined responses for general queries
    if "symptom" in user_input.lower():
        return "Please consult a doctor for more accurate advice.", False
    elif "appointment" in user_input.lower():
        return "Would you like to schedule an appointment with the doctor?", False
    elif "medication" in user_input.lower():
        return "It's important to take prescribed medicines regularly. If you have further concerns, consult a doctor.", False
    
    # Use Gemini for general queries
    try:
        response = model.generate_content(user_input)
        return response.text, False
    except Exception as e:
        return f"An error occurred while processing your query: {str(e)}", False

# Main function
def main():
    st.title("🤖 Healthcare Assistant Chatbot")
    st.markdown("Welcome to the Healthcare Assistant! How can I help you today?")
    
    # User input
    user_input = st.text_input("Enter your query:", placeholder="Type your message here...")
    
    # Submit button
    if st.button("Submit"):
        if user_input:
            st.write("**You:** ", user_input)
            with st.spinner("Processing your query, please wait..."):
                response, is_critical = healthcare_chatbot(user_input)
            
            if is_critical:
                st.error("Critical Case Detected!")
                st.markdown(f"<div class='critical-warning'>{response}</div>", unsafe_allow_html=True)
            else:
                st.success("**Assistant:** " + response)
        else:
            st.warning("Please enter a message to get a response.")

# Run the app
if __name__ == "__main__":
    main()
