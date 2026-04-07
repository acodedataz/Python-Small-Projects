# Python Project: Guess the Number Game__03
# Massive Interactive Version

import random
import time

print("🎮 Welcome to the SUPER Guess the Number Game! 🎮")
print("I have selected a number between 1 and 200.")
print("Try to guess it. Good Luck!\n")

# Random number selection
Random_Number = random.randint(1, 200)

# Optionally show random number for testing
show_number = input("Do you want to see the secret number? (y/n): ").lower()
if show_number == 'y':
    print(f"🔑 Secret Number is: {Random_Number}\n")

attempts = 0
level = 1

while True:
    try:
        User_Input = int(input(f"Level {level} - Enter your guess: "))
        attempts += 1

        # Massive feedback system
        if User_Input > Random_Number:
            print("🔺 Too High! Try a smaller number.")
        elif User_Input < Random_Number:
            print("🔻 Too Low! Try a bigger number.")
        else:
            print(f"\n🎉🎊 Congratulations! 🎊🎉")
            print(f"You guessed the number {Random_Number} correctly in {attempts} attempts!")
            print(f"💪 Total Levels Cleared: {level}")
            break  # Exit loop if guessed correctly

        # Extra hints based on difference
        diff = abs(Random_Number - User_Input)
        if diff <= 5:
            print("🔥 Very close! You are almost there!")
        elif diff <= 15:
            print("🌟 Close! Keep trying!")
        else:
            print("❄️ Far away! Try a bigger change.\n")

        # Optional level increase
        if attempts % 3 == 0:
            level += 1
            print(f"🚀 Level Up! You are now on Level {level}!\n")

        time.sleep(0.5)  # Small delay for better feel

    except ValueError:
        print("⚠️ Please enter a valid integer number.\n")