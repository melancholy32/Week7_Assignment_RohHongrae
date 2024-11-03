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
    return "We're sorry for your inconvenience. Customer service will contact you ASAP to help resolve the issue or provide compensation."
def external_negative_response(feedback):
    return "We're sorry for your experience. Unfortunately, we're not liable for such cases, but we’ll see how we can assist."
def positive_response(feedback):
    return "Thank you for your feedback and for choosing to fly with us! We hope to see you again!"

internal_negative_condition = lambda feedback: "lost luggage" in feedback or "rude staff" in feedback
external_negative_condition = lambda feedback: "weather" in feedback or "delay" in feedback
positive_condition = lambda feedback: not internal_negative_condition(feedback) and not external_negative_condition(feedback)

branch = RunnableBranch(
    (internal_negative_condition, internal_negative_response),
    (external_negative_condition, external_negative_response),
    (positive_condition, positive_response),
    lambda feedback: "Thank you for your feedback. We'll make sure to improve for your next flight."  # Default branch
)

def process_feedback(feedback):
    response = branch.invoke(feedback)
    st.write(response)

if st.button("Submit"):
    process_feedback(feedback)
if st.button("Submit"):
  process_feedback(feedback)
