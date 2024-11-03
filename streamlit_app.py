# Streamlit URL: https://rohhongrae-week7.streamlit.app/
# Github URL: https://github.com/melancholy32/Week7_Assignment_RohHongrae

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables.branch import RunnableBranch
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables.branch import RunnableBranch

st.title("💬 Chatbot for your flight experience")
st.write("Please share with us your experience of the latest trip. Your feedback is really important for us.")
feedback = st.text_area("Share with us your experience of the latest trip.")

openai_api_key = "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"
llm = ChatOpenAI(openai_api_key=openai_api_key)

def internal_negative_response(feedback):
    prompt = f"Apologize empathetically to a customer who experienced issues with their recent trip due to airline-related problems like '{feedback}'. Provide a response that shows understanding and assures customer service follow-up."
    response = llm.predict(prompt)
    return response

def external_negative_response(feedback):
    prompt = f"Sympathize with a customer who experienced a delay or inconvenience due to factors beyond the airline's control, such as '{feedback}'. Offer support without taking responsibility."
    response = llm.predict(prompt)
    return response

def positive_response(feedback):
    prompt = f"Thank the customer for their positive feedback about their recent trip experience. Mention appreciation and express a desire to serve them again. Their feedback was: '{feedback}'."
    response = llm.predict(prompt)
    return response

internal_negative_condition = lambda feedback: "lost luggage" in feedback or "rude staff" in feedback
external_negative_condition = lambda feedback: "weather" in feedback or "delay" in feedback
positive_condition = lambda feedback: not internal_negative_condition(feedback) and not external_negative_condition(feedback)

branch = RunnableBranch(
    (internal_negative_condition, internal_negative_response),
    (external_negative_condition, external_negative_response),
    (positive_condition, positive_response),
    lambda feedback: "Thank you for your feedback. We'll make sure to improve for your next flight.")

def process_feedback(feedback):
    response = branch.invoke(feedback)
    st.write(response)

if st.button("Submit"):
    process_feedback(feedback)
