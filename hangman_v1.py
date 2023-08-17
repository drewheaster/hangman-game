# importing the time module
import time

answer = 'foxes'

print('Welcome to Hangman! What is your name?')

name = input('Enter name: ')

time.sleep(1)
print('Ready to play, ' + name + '?')
time.sleep(1)
print('Let us begin...')
time.sleep(1)
print('There are ' + str(len(answer)) + ' letters. You have 5 chances to guess the answer. Take your first guess!')
time.sleep(1.5)

turns = 5

def new_block(answer):
    block = ''
    for i in range(len(answer)):
        block += '_'
    return block

def turn_counter(turns):
    empty_block = new_block(answer)
    guess = input('Guess a letter: ')
    while turns >= 0:
        if guess in answer:
            print('Correct! You have ' + str(turns) + ' turns left.')
            time.sleep(1)
            position = answer.index(str(guess))
            empty_block = empty_block[:position] + guess + empty_block[position+1:]
            print(empty_block)
            if empty_block == answer:
                return print('Sweet! The answer is ' + empty_block + '. Congrats! You won!') 
            guess = input('Guess another letter: ')
        if guess not in answer:
            turns -= 1
            print('Incorrect... You have ' + str(turns) + ' turns left.')
            time.sleep(1)
            print(empty_block)
            guess = input('Guess again: ')
        if turns == 0:
            print('You have run out of turns. Game over.')
            return turns

turn_counter(turns)

time.sleep(1)

redo = input('Would you like to play again? Y or N: ')

def restart(redo):
    if redo == 'y':
        turns = 5
        turn_counter(turns)
    else:
        return print('See you again soon, ' + name + '!')

restart(redo)