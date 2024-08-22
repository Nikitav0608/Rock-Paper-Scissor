import random

# Print multiline instruction with emojis
print('\n🎮 Winning Rules of the Game: ROCK 🪨 PAPER 📄 SCISSORS ✂️   🎮\n'
      + "\n🪨 Rock vs Paper 📄 -> Paper 📄 wins \n"
      + "\n🪨 Rock vs Scissors ✂️ -> Rock 🪨 wins \n"
      + "\n📄 Paper vs Scissors ✂️ -> Scissors ✂️ wins \n")

while True:
    print("\nEnter your choice:\n"
          + "1 - Rock 🪨 \n"
          + "2 - Paper 📄 \n"
          + "3 - Scissors ✂️ \n")

    # Take the input from user
    choice = int(input("Enter your choice: "))

    # Loop until user enters a valid choice
    while choice > 3 or choice < 1:
        choice = int(input('😬 Enter a valid choice please 😬\n'))

    # Initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock 🪨'
    elif choice == 2:
        choice_name = 'Paper 📄'
    else:
        choice_name = 'Scissors ✂️'

    # Print user's choice
    print(f"\nUser choice is: {choice_name}")
    print("Now it's the Computer's Turn... 🤖")

    # Computer chooses randomly any number among 1, 2, and 3
    comp_choice = random.randint(1, 3)

    # Loop until comp_choice is different from user's choice to avoid a draw
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # Initialize value of comp_choice_name corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock 🪨'
    elif comp_choice == 2:
        comp_choice_name = 'Paper 📄'
    else:
        comp_choice_name = 'Scissors ✂️'

    # Print computer's choice
    print(f"\nComputer choice is: {comp_choice_name}")
    print(f"{choice_name} Vs {comp_choice_name}")

    # Determine the result
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper 📄'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock 🪨'
    else:
        result = 'Scissors ✂️'

    # Print the result
    if result == "DRAW":
        print("<== It's a Tie! 🤝 ==>")
    elif result == choice_name:
        print("<== 👏 User wins! 🥳 ==>")
    else:
        print("<== 🤖 Computer wins! 🎉 ==>")

    # Ask the user if they want to play again
    ans = input("\nDo you want to play again? (Y/N): ").lower()
    if ans == 'n':
        break

# After exiting the loop, print a thank you message
print("🙏 Thanks for Playing! 🙏")
