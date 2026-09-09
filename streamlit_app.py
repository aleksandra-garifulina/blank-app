import streamlit as st


st.title("Guess the dog breed")

items = ["labrador", "akita", "poodle", "podenco", "galgo", "german shepherd", "borzoi", "border collie", "Jack Russel terrier"]


guess = st.selectbox(
    "What do you think is my favourite one?",
    items,
    index=None,
    placeholder="select your guess..."
)


if st.button("Submit guess"):

    if guess == "podenco":
        st.success("Yess! 🐕")
        st.balloons()
    else:
        st.error("Nope :(, try again")


