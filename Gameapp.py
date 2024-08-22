import random
import streamlit as st

# Title of the app
st.title("Rock 🪨 Paper 📄 Scissors ✂️ Game")

# Display the rules
st.write("""
### 🎮 Winning Rules:
- 🪨 Rock vs 📄 Paper -> 📄 Paper wins
- 🪨 Rock vs ✂️ Scissors -> 🪨 Rock wins
- 📄 Paper vs ✂️ Scissors -> ✂️ Scissors wins
""")

# Function to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a Tie! 🤝"
    elif (user_choice == 'Rock 🪨' and comp_choice == 'Scissors ✂️') or \
         (user_choice == 'Paper 📄' and comp_choice == 'Rock 🪨') or \
         (user_choice == 'Scissors ✂️' and comp_choice == 'Paper 📄'):
        return "You win! 🥳"
    else:
        return "Computer wins! 🎉"

# Get user choice using a radio button
user_choice = st.radio("Choose your option:", ['Rock 🪨', 'Paper 📄', 'Scissors ✂️'])

# Play the game when the user clicks the button
if st.button("Play!"):
    comp_choice = random.choice(['Rock 🪨', 'Paper 📄', 'Scissors ✂️'])

    # Display the choices
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {comp_choice}")

    # Determine and display the result
    result = determine_winner(user_choice, comp_choice)
    st.write(f"**Result:** {result}")

# Closing message
st.write("🙏 Thanks for Playing! 🙏")
