import os
import sys
import random


class Game:

    def __init__(self, word_list=None):
        # make sure a wordlist is passed to obj
        assert word_list, 'No wordlist found!'

        self.runtime = False
        self.words = []
        self.word = ''
        self.word_so_far = ''
        self.attempts = 0
        self.max_attempts = 5
        self.guesses = []

        try:
            # add words from word_list to words and pull off the newline character
            with open(word_list, 'r') as f:
                for word in f:
                    self.words.append(word.strip())
        except FileNotFoundError as e:
            sys.stderr.write(str(e))
            quit()

        # make sure word_list actually has some form of words
        assert self.words, f'Error reading word list, please check file : {word_list}'

        self.word = random.choice(self.words)
        self.word_so_far = ['_' for x in range(len(self.word))]

    def print_stats(self):
        # Inform user of current state of game
        # Attempts, letters used, and position of correct guesses
        print('Enter quit to exit or enter your guess!')
        print()

        print(f'{self.attempts} attempts of {self.max_attempts}')
        print(f'Letters used : ', end='')
        for used in self.guesses:
            print(used, end=' ')
        print()

        print(f'Word : ', end='')
        for i in self.word_so_far:
            print(i + ' ', end='')
        print('\n')

    def congratulate(self):
        os.system('clear')

        print('Congratulations! You guessed the word correctly!')
        print(f'The word was {self.word}')
        quit()

    def check_guess(self, guess):
        if guess == 'quit':
            os.system('clear')
            self.print_stats()
            print()
            print('Thank you for playing Hangman!')
            print(f'The correct word was : {self.word}')
            quit()
        elif guess == self.word:
            self.congratulate()
        elif len(guess) > 1 or len(guess) == 0:
            print('Please enter in ONE letter! This counts as an attempt!')
        elif guess in '0123456789':
            print('Please enter in a LETTER! This counts as an attempt!')
        elif guess in self.guesses:
            print('You\'ve already entered in that guess! This counts as an attempt!')
        else:
            counter = 0

            for letter in self.word:
                if letter == guess:
                    self.word_so_far[counter] = guess

                counter += 1

            self.guesses.append(guess)

        self.attempts += 1

    def start_game(self):
        start_game = input('Would you like to play hangman? [y/N] ').lower()

        if start_game == 'y' or start_game == 'yes':
            self.runtime = True
        else:
            quit()

        os.system('clear')

        print('You have 5 attempts, choose carefully!')
        print()

        while self.attempts < self.max_attempts:
            self.print_stats()
            print()

            guess = input('Guess: ').lower()
            os.system('clear')

            self.check_guess(guess)

        print('OH, NO! You ran out of attempts!')
        print(f'The correct word was: {self.word}')
