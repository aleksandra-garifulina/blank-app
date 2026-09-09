import streamlit as st
import random
import pandas as pd

tab1, tab2, tab3 = st.tabs(["guess the breed", "trivia", "3rd thingy"])

with tab1:

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
        elif guess == "poodle":
            st.error("Nope! but I love the fluff")
        elif guess == "galgo":
            st.error("Nope, but you are close")
        else:
            st.error("Nope :(, try again")



# DATA

breeds = [
    {
        "name": "Podenco",
        "year": -3800,
        "speed": 64,
    },

    {
        "name": "Greyhound",
        "year": -5000,
        "speed": 72,
    },

    {
        "name": "Saluki",
        "year": -6000,
        "speed": 68,
    },

    {
        "name": "Basenji",
        "year": -3500,
        "speed": 40,
    },

    {
        "name": "Whippet",
        "year": 1800,
        "speed": 56,
    },

    {
        "name": "French Bulldog",
        "year": 1800,
        "speed": 27,
    },

]

# HELPER


def format_year(year):
    if year < 0:
        return f"{abs(year)} BCE"
    elif year > 0:
        return f"{year} CE"
    else:
        return "1 CE"

#--------
# TAB 2

with tab2:

    st.write("### Dog Trivia")

    # Pick two independent random dogs

    if "year_breed" not in st.session_state:
        st.session_state.year_breed = random.choice(breeds)
    if "speed_breed" not in st.session_state:
        st.session_state.speed_breed = random.choice(breeds)

    year_breed = st.session_state.year_breed
    speed_breed = st.session_state.speed_breed

    col1, col2 = st.columns(2)
 

    # QUESTION 1 — HISTORY


    with col1:

        st.write("### 🏺 Ancient Origins")
        st.write(
            f"When do you think the **{year_breed['name']}** "
            f"was first documented?"
        )

        # Get all historical dates from the breed data

        year_options = sorted(
            set(breed["year"] for breed in breeds)
        )

        year_guess = st.select_slider(
            "Choose a year:",
            options=year_options,
            format_func=format_year,
        )

        st.caption(f"Your guess: **{format_year(year_guess)}**")


        if st.button("Submit year", key="year_button"):

            correct_year = year_breed["year"]
            # Correct answer

            if year_guess == correct_year:
                # Special Podenco answer
                if year_breed["name"] == "Podenco":
                    st.success(
                        "You're right! 🏺🐕 "
                        "Dogs resembling Podencos appear in Egyptian tomb "
                        "paintings from around **3800 BCE**."
                    )

                else:
                    st.success(
                        f"You're right! 🐕 "
                        f"The {year_breed['name']} dates back to around "
                        f"**{format_year(correct_year)}**."
                    )

            # User guessed an earlier date

            elif year_guess < correct_year:
                st.warning(
                    "Nope — a bit younger! 👀"
                )

            # User guessed a later date

            else:
                st.warning(
                    "Nope — a bit older! 👀"
                )


    # QUESTION 2 — SPEED


    with col2:

        st.write("### 💨 Speed Challenge")
        st.write(
            f"Which breed can reach approximately "
            f"**{speed_breed['speed']} km/h**?"
        )
        breed_names = [breed["name"] for breed in breeds]
        
        speed_guess = st.radio(
            "Choose a breed:",
            breed_names,
            index=None,
)


        if st.button("Submit answer", key="speed_button"):
            if speed_guess is None:
                st.warning("Choose a breed first!")

            elif speed_guess == speed_breed["name"]:

                st.success(
                    f"Correct! 🐕💨 "
                    f"{speed_breed['name']} can reach approximately "
                    f"**{speed_breed['speed']} km/h**."
                )

            else:
                st.error(
                    f"hmm no"
                )



    # NEW QUESTIONS

    st.divider()

    if st.button("🔄 wanna guess one more time"):

        st.session_state.year_breed = random.choice(breeds)
        st.session_state.speed_breed = random.choice(breeds)
        st.rerun()


# PANDA DF

st.divider()

with st.expander("📊 Show breed data"):
    df = pd.DataFrame(breeds)
    st.dataframe(df, use_container_width=True)
