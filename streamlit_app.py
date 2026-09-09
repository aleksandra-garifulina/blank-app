import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.title("Guess the author's (mine hehe) favourite dog breed")

items = ["labrador", "akita", "poodle", "podenco", "galgo", "german shepherd", "borzoi", "border collie", "Jack Russel terrier"]

guess = st.selectbox("What do you think is my favourite?", items)

if st.button("Submit guess"):

    if guess == "podenco":
        st.success("Yess! 🐕")
        st.balloons()
    else:
        st.error("Nope :(, try again")
        
