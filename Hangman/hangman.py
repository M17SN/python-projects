# importing and initialize variables
import random
from words import words
from drawings import stages, logo
random_word = random.choice(words)

display = []
for i in range(len(random_word)):
    display.append("_")


random_word_as_list = []
for i in range(len(random_word)):
    random_word_as_list.append(random_word[i])

end_of_game = False
lives = 6
# start the game
print(logo)
while not end_of_game and lives > -1:
    guess = input("Guess a letter: ")
    if random_word.lower().count(guess.lower()) == 0:
        print(stages[lives])
        print(display)
        lives -= 1
    else:
        for i in range(len(random_word_as_list)):
            if random_word_as_list[i].lower() == guess.lower():
                index = random_word_as_list.index(random_word_as_list[i])
                display[i] = guess
        print(display)
    if "_" not in display:
        end_of_game = True

if lives != -1:
    print("You got it! it is " + random_word)
else:
    print("You lost! it is " + random_word)