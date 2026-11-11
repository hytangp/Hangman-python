import random

word_list = ["jazz", "buzz", "camel", "ostrich", "heaven", "dangerous", "esophagus", "unravel"]

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
display = ["_"]*len(chosen_word)

#print(chosen_word)
print("".join(display))

left_lives_count = len(stages)
guessed_letters = []

while left_lives_count > 0 and "".join(display) != chosen_word:
    guess = input("Guess a letter: ").lower()
    previous_missing_letter_count = display.count("_")

    if guess in guessed_letters:
        print("You already guessed this letter. Choose another letter.")
    else:
        guessed_letters.append(guess)
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter

        current_missing_letter_count = display.count("_")

        if current_missing_letter_count == previous_missing_letter_count:
            left_lives_count-=1
            print(stages[left_lives_count])
            print("****************************" + str(left_lives_count) + " LIVES LEFT****************************")

        print("".join(display))

if left_lives_count > 0:
    print("You win! You guessed the word!")
else:
    print("Game Over! Correct word was: " + chosen_word)
