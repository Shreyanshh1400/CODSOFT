import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Score variables
user_score = 0
computer_score = 0

print("=" * 40)
print("      ROCK - PAPER - SCISSORS")
print("=" * 40)
print("Instructions:")
print("- Type Rock, Paper, or Scissors.")
print("- Type 'quit' anytime to exit the game.\n")

while True:
    # User input
    user_choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()

    if user_choice == "quit":
        print("\nThanks for playing!")
        break

    if user_choice not in choices:
        print("❌ Invalid choice! Please choose Rock, Paper, or Scissors.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose      : {user_choice.capitalize()}")
    print(f"Computer chose : {computer_choice.capitalize()}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1

    else:
        print("💻 Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nCurrent Score")
    print("----------------")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n========== Final Score ==========")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

        if user_score > computer_score:
            print("🏆 Congratulations! You won the game!")
        elif computer_score > user_score:
            print("💻 Computer won the game!")
        else:
            print("🤝 The game ended in a tie!")

        print("\nThank you for playing!")
        break