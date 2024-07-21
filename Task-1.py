import random

words = ['Thor', 'CaptainAmerica', 'SpiderMan', 'IronMan', 'AntMan', 'Thanos', 'Hulk','BrushBanner']
word = random.choice(words)
guessed = ['_'] * len(word)
incorrect_guesses_allowed = 6
incorrect_guesses = 0

print("Welcome to Hangman!")
print("You have", incorrect_guesses_allowed, "chances to guess the word.")

while True:
    print(' '.join(guessed))

    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        incorrect_guesses += 1
        print("Incorrect guess. You have", incorrect_guesses_allowed - incorrect_guesses, "chances left.")

    if '_' not in guessed:
        print(' '.join(guessed))
        print("Congratulations, you won!")
        break

    if incorrect_guesses == incorrect_guesses_allowed:
        print("You lost. The word was", word)
        break