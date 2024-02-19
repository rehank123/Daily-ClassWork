import streamlit as st

def health_chatbot():
    st.title("Health Chatbot")

    st.sidebar.title("User Input")
    user_input = st.sidebar.text_area("Enter your message")

    if st.sidebar.button("Ask"):
        bot_response = get_bot_response(user_input)
        st.write("Bot:", bot_response)

def get_bot_response(user_input):
    # Simple rule-based responses
    if "symptoms" in user_input.lower():
        return "Please consult a doctor for accurate diagnosis and treatment."
    elif "fever" in user_input.lower():
        return "Fever could be a sign of an underlying condition. Make sure to stay hydrated and rest. If it persists, consult a doctor."
    elif "headache" in user_input.lower():
        return "Headaches can be due to various reasons. Ensure you're well-hydrated and consider taking a break if you've been staring at screens for too long."
    else:
        return "I'm sorry, I couldn't understand that. Please provide more information or rephrase your question."

if __name__ == "__main__":
    health_chatbot()
