import streamlit as st
import random

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
        "year_min": -3800,
        "year_max": -3600,
        "speed": 64,
    },

    {
        "name": "Greyhound",
        "year_min": -5000,
        "year_max": -5000,
        "speed": 72,
    },

    {
        "name": "Saluki",
        "year_min": -6000,
        "year_max": -6000,
        "speed": 68,
    },

    {
        "name": "Basenji",
        "year_min": -3500,
        "year_max": -3500,
        "speed": 40,
    },

    {
        "name": "Whippet",
        "year_min": 1800,
        "year_max": 1800,
        "speed": 56,
    },

    {
        "name": "French Bulldog",
        "year_min": 1800,
        "year_max": 1800,
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

        year_guess = st.slider(
            "Choose a year:",
            min_value=-6000,
            max_value=2000,
            value=-3000,
            step=100,
        )

        st.caption(f"Your guess: **{format_year(year_guess)}**")

        if st.button("Submit year", key="year_button"):
            correct_min = year_breed["year_min"]
            correct_max = year_breed["year_max"]

            if correct_min <= year_guess <= correct_max:

                # Special Podenco feedback
                if year_breed["name"] == "Podenco":
                    st.success(
                        "You're right! 🏺🐕 "
                        "Dogs resembling Podencos appear in Egyptian tomb paintings from around **3800-3600 BCE**."
                    )
                 

                else:

                    st.success(
                        f"You're right! 🐕 "
                        f"The {year_breed['name']} dates back to around "
                        f"**{format_year(correct_min)}**."
                    )
                    
                

            elif year_guess < correct_min:

                st.warning(
                    "nope, they are not that old! 👀"
                )

            elif year_guess < correct_max:

                st.warning(
                    "You're getting closer 👀"
                )
            else:
                st.error(
                    "Nope — that's too recent!"
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

