# Python Text-Based Adventure Game: Project__04

import time

def delay_print(message, delay=1.0):
    """Print message with a small delay for dramatic effect"""
    print(message)
    time.sleep(delay)

# Welcome
answer = input("🕹️ Do You Want To Play This Adventure Game? [Yes/No] ").strip().lower()
if answer == "yes":
    delay_print("🎉 Welcome to the Adventure Game!", 1.2)
    delay_print("🌿 You are about to make your first choice...", 1.0)

    choice1 = input("Do You Want To Go to Jungle or Cave? [Jungle/Cave] ").strip().lower()

    if choice1 == "jungle":
        delay_print("🌳 You walk into the jungle...", 1.0)
        delay_print("🐯 Oh no! Hungry Tigers appear!", 1.2)
        delay_print("⚠️ Tiger is too strong. You couldn't survive. Game Over!", 1.5)

    elif choice1 == "cave":
        delay_print("🪨 You approach the dark cave...", 1.0)
        delay_print("🐻 A wild bear appears at the entrance!", 1.2)

        choice2 = input("Do You Want To Fight the Bear or Run Away? [Fight/Run] ").strip().lower()
        if choice2 == "fight":
            delay_print("⚔️ You try to fight the bear...", 1.0)
            delay_print("💥 The bear is too strong!", 1.0)
            delay_print("💀 You lost the battle. Game Over!", 1.5)
        elif choice2 == "run":
            delay_print("🏃 You run away skillfully!", 1.0)
            delay_print("🎉 Wow! You survived and escaped the cave safely!", 1.2)
        else:
            delay_print("❌ Invalid choice! The bear attacks you. Game Over.", 1.2)
    else:
        delay_print("❌ Invalid path! You got lost and the adventure ends here.", 1.2)

else:
    delay_print("👋 The game is closed. Maybe next time!", 1.0)