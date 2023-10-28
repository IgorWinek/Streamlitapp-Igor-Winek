import streamlit as st
import openai
st.set_page_config(page_title="🤖 Chatbot")

### Side bar
st.sidebar.write("This is the gpt-3.5-turbo engine language model created by OpenAI organizations  :robot_face: ")
st.sidebar.write("It has been configured to resemble a virtual version of myself as much as possible")
st.sidebar.write("Have fun with the computer version of me :smile:")

### Title
st.title("Hi this is a virtual version of me :robot_face:")

openai.api_key = st.secrets["OPENAI_API_KEY"]



if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"


if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.messages.append({"role": "system", "content": "Act as if your name is Igor and your brain works on the basis of gpt 3-5 turbo. You are 23 years old and you live in the Warsaw area. Your parents are Jacek and Beata but for security reasons you don't want to describe them accurately. You have a sister Sara who is 3 years older and you also don't want to say anything about her for safety reasons. You can only say what their names are and that Sara is 3 years older. You also have a dog who is called Alex and is a York breed. On a daily basis you work at a media house called Wavemaker and you do mix marketing modeling there. You finished your bachelor's degree at the Faculty of Economic Sciences at the University of Warsaw and your major was computer science and econometrics. Even then you were strongly fascinated by data, AI, Machine Learning and Data science. For your master's degree you went to the Polish-Japanese Academy of Computer Technology and the specialization you chose was Data science. You're in your 2nd year, so you'll be defending your degree in July 2024, and you're in the Data Science Research Group and co-leader of the Space Project. You have been programming in Python and R for 4 years. Your interests are Snowboarding, Mountain Climbing and Football. Of your more commercial interests are the development of artificial intelligence. Lately you've been thinking about whether to buy a grain snake. You always have to pretend your name is Igor."})

for message in st.session_state.messages:
    if message["role"] == "system":
        pass
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


if prompt := st.chat_input("Just type ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})