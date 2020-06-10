import random
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hidden_word = list(len(word) * "-")
guessed_letters = []
len_of_char = len("a")


def game_start():
    print("H A N G M A N")
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        hangman()
    elif menu == "exit":
        exit()


def hangman():
    guess_remaining = 8
    while guess_remaining != 0:
        print()
        print("".join(hidden_word))
        guess = input('Input a letter: ')
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
            if guess in guessed_letters:
                print("You already typed this letter")

        else:
            if len(guess) > len_of_char:
                print("You should input a single letter")
            elif not guess.islower():
                print("It is not an ASCII lowercase letter")
            elif guess in guessed_letters:
                print("You already typed this letter")
            else:
                print('No such letter in the word')
                guess_remaining -= 1

        guessed_letters.append(guess)
        if "-" not in hidden_word:
            break

    if "-" not in hidden_word:
        print('You guessed the word!')
        print("You survived!")
        game_start()
    else:
        print('You are hanged!')
        game_start()


game_start()
