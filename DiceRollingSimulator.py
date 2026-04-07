# Python Dice Rolling Simulator Game Project__05 (Updated Version)

import random
import time

print("🎲 Welcome to the Dice Rolling Simulator! 🎲\n")
print("Roll the dice and see if you can get a high number!\n")

high_score = 0  # Track the highest roll

while True:
    input("Press Enter to roll the dice...")
    print("Rolling", end="", flush=True)

    # Dice rolling animation
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)

    dice = random.randint(1, 6)
    print(f"\nYou rolled a {dice}!")

    # Update high score if needed
    if dice > high_score:
        high_score = dice
        print(f"🎉 Congratulations! New high score: {high_score}!")
    else:
        print(f"Your current high score: {high_score}")

    # Ask if the player wants to roll again
    while True:
        PlayAgain = input("Do you want to roll again? [Y/N]: ").strip().upper()
        if PlayAgain in ["Y", "N"]:
            break
        else:
            print("❌ Invalid input! Please type Y or N.")

    if PlayAgain == "N":
        print("\nGame Over! Thanks for playing. 🎲")
        break