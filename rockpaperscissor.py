import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)
        display_result(user, computer, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nScore -> You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

play_game()
