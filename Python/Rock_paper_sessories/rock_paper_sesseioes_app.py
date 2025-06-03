import streamlit as st
import random

# ASCII art for the game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

# UI
st.title("🪨📄✂️ Rock Paper Scissors Game")
st.markdown("Play against the computer and test your luck!")

user_choice = st.selectbox("Choose your option:", choices)

if st.button("Play"):
    user_index = choices.index(user_choice)
    computer_index = random.randint(0, 2)

    st.subheader("Your Choice:")
    st.code(game_images[user_index])

    st.subheader("Computer's Choice:")
    st.code(game_images[computer_index])

    if user_index == computer_index:
        result = "🤝 It's a Tie!"
    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        result = "🎉 You Win!"
    else:
        result = "💻 You Lose."

    st.success(result)
