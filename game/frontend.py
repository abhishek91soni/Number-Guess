import streamlit as st
from rps import Play_round

st.title("Rock Paper Scissors")

choices = ["rock", "paper", "scissors"]

# Session state
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.draws = 0

user_input = st.selectbox("Choose your move:", choices)

if st.button("Play"):
    computer_pick, result = Play_round(user_input)

    st.write(f"🤖 Computer picked: **{computer_pick}**")

    if result == "win":
        st.success("You Won! 🎉")
        st.session_state.player_wins += 1

    elif result == "lose":
        st.error("You Lost! 😢")
        st.session_state.computer_wins += 1

    else:
        st.info("It's a Draw!")
        st.session_state.draws += 1

st.markdown("---")
st.subheader("📊 Scoreboard")

st.write(f"Player Wins: {st.session_state.player_wins}")
st.write(f"Computer Wins: {st.session_state.computer_wins}")
st.write(f"Draws: {st.session_state.draws}")

if st.button("Reset Score"):
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.draws = 0
    st.success("Score Reset!")