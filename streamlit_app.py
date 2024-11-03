# Streamlit URL: https://rohhongrae-week7.streamlit.app/
# Github URL: https://github.com/melancholy32/Week7_Assignment_RohHongrae

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables.branch import RunnableBranch

st.title("💬 Chatbot for your flight experience")
st.write("Please share with us your experience of the latest trip. Your feedback is really important for us.")
feedback = st.text_area("Share with us your experience of the latest trip.")


openai_api_key = "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"
llm = ChatOpenAI(openai_api_key=openai_api_key)

def internal_negative_response(feedback):
    prompt = f"Apologize empathetically to a customer who experienced issues with their recent trip due to airline-related problems like '{feedback}'. Provide a response that shows understanding and assures customer service follow-up."
    response = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Generate a polite, empathetic response to the user's complaint. Tell the user that Customer service will contact you ASAP to help you solve issue or provide compensation."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

def external_negative_response(feedback):
    prompt = f"Sympathize with a customer who experienced a delay or inconvenience due to factors beyond the airline's control, such as '{feedback}'. Offer support without taking responsibility."
    response = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Generate a sympathetic response acknowledging the user's inconvenience. Tell the user that we're not liable for such cases, but will figure out how we can help you with the situation"},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

def positive_response(feedback):
    prompt = f"Thank the customer for their positive feedback about their recent trip experience. Mention appreciation and express a desire to serve them again. Their feedback was: '{feedback}'."
    response = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Generate a friendly and appreciative response to the user's positive feedback. Tell the user that we thank you for the feedback and for choosing to fly with us! We hope to see you again."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

# Define conditions as boolean checks
internal_negative_condition = lambda feedback: "lost luggage" in feedback or "rude staff" in feedback
external_negative_condition = lambda feedback: "weather" in feedback or "delay" in feedback
positive_condition = lambda feedback: not internal_negative_condition(feedback) and not external_negative_condition(feedback)

# Setup the RunnableBranch with conditions and dynamic responses
branch = RunnableBranch(
    (internal_negative_condition, internal_negative_response),
    (external_negative_condition, external_negative_response),
    (positive_condition, positive_response),
    lambda feedback: "Thank you for your feedback. We'll make sure to improve for your next flight."  # Default branch
)

# Define the process_feedback function to handle feedback submission
def process_feedback(feedback):
    response = branch.invoke(feedback)
    st.write(response)

# Trigger feedback processing on button click
if st.button("Submit"):
    process_feedback(feedback)
