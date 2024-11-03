import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables.branch import RunnableBranch

st.title("💬Chatbot for your flight experience")
st.write("Please share with us your experience of the latest trip. Your feedback is really important for us.")
feedback = st.text_area("Share with us your experience of the latest trip.")

if st.button("Submit"):
  process_feedback(feedback)
  
### Get the OpenAI API key
from google.colab import userdata
openai_api_key = userdata.get('MyOpenAIKey')

### Create a ChatOpenAI object
llm = ChatOpenAI(openai_api_key=openai_api_key)




# Show title and description.
# st.title(" Chatbot for your experience")
# st.write(
#     "Please share your experience with our flight and service. Your feedback is really important for us."
)

#OpenAI API Key
# from langchain.chat_models import ChatOpenAI

### Get the OpenAI API key
# from google.colab import userdata
# openai_api_key = userdata.get('MyOpenAIKey')

### Create a ChatOpenAI object
# chat = ChatOpenAI(openai_api_key=openai_api_key)


# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

    # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
  #   for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
      #       st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
 #            st.markdown(prompt)

        # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
 #            messages=[
    #             {"role": m["role"], "content": m["content"]}
   #              for m in st.session_state.messages
 #            ],
  #           stream=True,
  #       )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
 #        with st.chat_message("assistant"):
 #            response = st.write_stream(stream)
 #        st.session_state.messages.append({"role": "assistant", "content": response})
