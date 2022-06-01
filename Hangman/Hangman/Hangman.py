import random
import re

words = ['python', 'java', 'swift', 'javascript']
win = 0
loss = 0
max_attempts = 8


print('H A N G M A N\n')
while True:
    word = random.choice(words)
    cur_attempt = 1
    hint_word = ['-' for letter in list(word)]
    used_letters = set()
    button = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if button == 'play':
        print('\n')
        while cur_attempt <= max_attempts:
            print(''.join(hint_word))
            answer = input('Input a letter: ')
            if len(answer) == 1:
                if answer.lower() == answer and answer.isalpha():
                    if answer in used_letters:
                        cur_attempt -= 1
                        print('You\'ve already guessed this letter.\n')
                        continue
                    if answer in word:
                        cur_attempt -= 1
                        for match in re.finditer(answer, word):
                            hint_word[match.start()] = answer
                        print('\n')
                        if ''.join(hint_word) == word:
                            win += 1
                            print(word, '\nYou guessed the word {0}!\nYou survived!'.format(word))
                            break
                    else:
                        print('That letter doesn\'t appear in the word.\n')
                    cur_attempt += 1
                    used_letters.add(answer)
                else:
                    print('Please, enter a lowercase letter from the English alphabet.\n')
            else:
                print('Please, input a single letter.\n')
        else:
            loss += 1
            print('\n{0}'.format('You lost!'))
    elif button == 'results':
        print('You won: {0} times\nYou lost: {1} times'.format(win, loss))
    elif button == 'exit':
        break
    else:
        continue
