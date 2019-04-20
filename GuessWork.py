# TO DO:
#  -Let cpu choose a random item and make it the only correct answer.
#  -Instead of "Guess a word", give a hint about an item like "It's a fruit and it's red. What am I thinking about?"

def GuessWork():
    print("Welcome to \"Guesswork\" game.\n")

    GameOn = True

    while GameOn:

        words = ["apple", "berry", "pineapple", "strawberry"]
        guess = ""
        ValidGuess = False

        while not ValidGuess:
            guess = input("Guess a word: ").lower()

            if guess not in words:
                print("Try again")
            else:
                ValidGuess = True
                print("You guessed!\n")
                GameOn = False
        while not GameOn:
            result = input("Play again? (y/n): ").lower()
            if result == "no" or result == "n":
                break
            elif result == "yes" or result == "y":
                GameOn = True
            else:
                print("Wrong input")
GuessWork()
