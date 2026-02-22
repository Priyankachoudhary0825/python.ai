import random

user_score = 0
computer_score = 0
rounds = 0

choices = ["rock", "paper", "scissors"]

while True:
    rounds += 1
    print("\nRound:", rounds)

    user = input("Rock, Paper ya Scissors choose karein: ").lower()

    if user not in choices:
        print(" Galat choice! Dobara try karein.")
        rounds -= 1
        continue

    computer = random.choice(choices)

    print("User choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print(" Tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("User wins this round!")
        user_score += 1
    else:
        print(" Computer wins this round!")
        computer_score += 1

    play_again = input("\nDobara game khelni hai? (yes/no): ").lower()

    if play_again != "yes":
        break

# Final Result
print("\n====== GAME OVER ======")
print("Total Rounds:", rounds)
print("User Wins:", user_score)
print("Computer Wins:", computer_score)

# Save score to file
with open("score.txt", "a") as file:
    file.write("Rock Paper Scissors Game Result\n")
    file.write(f"Rounds: {rounds}\n")
    file.write(f"User Wins: {user_score}\n")
    file.write(f"Computer Wins: {computer_score}\n")
    file.write("------------------------\n")

print("\n Score file me save ho gaya (score.txt)")

