# Python Hangman Game Project__06

Secret_Word = "Shanto"
Chance = 5
Guessed_Letters = []
Game_Won = False

print("Welcome to Hangman Game!")
print(f"You have {Chance} chances to guess the word.\n")

while Chance > 0 and not Game_Won:
    Display_Word = ""
    for letter in Secret_Word:
        if letter.lower() in Guessed_Letters:
            Display_Word += letter + " "
        else:
            Display_Word += "_ "
    print("\nWord: ", Display_Word.strip())

    MyGuess = input(f"\nYou have {Chance} chances left. Guess a letter: ").lower()

    if MyGuess in Guessed_Letters:
        print("You already guessed that letter!")
        continue

    Guessed_Letters.append(MyGuess)

    if MyGuess not in Secret_Word.lower():
        Chance -= 1
        print(f"Wrong guess! {Chance} chance(s) left.")

    # Check if all letters are guessed
    Game_Won = all(letter.lower() in Guessed_Letters for letter in Secret_Word)

if Game_Won:
    print(f"\n🎉 Congratulations! You guessed the word: {Secret_Word}")
else:
    print(f"\n😢 You lost! The word was: {Secret_Word}")