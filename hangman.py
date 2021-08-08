from random import choice

with open('word_list.txt', 'r') as file:
    words = file.readlines()

secret_word = choice(words)[:-1]

allowed_guesses = 8
guesses = []
game_over = False

while not game_over:
    for char in secret_word:
        if char.lower() in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
    print('')

    guess = str(input(f'Guesses left: {allowed_guesses}\nGuess: '))
    guesses.append(guess.lower())

    if guess.lower() not in secret_word.lower():
        allowed_guesses -= 1
        if allowed_guesses == 0:
            break

    game_over = True

    for letter in secret_word:
        if letter.lower() not in guesses:
            game_over = False
if game_over:
    print(f'You guessed it, the word was {secret_word}!')
else:
    print(f'Game over, the word was {secret_word}!')
