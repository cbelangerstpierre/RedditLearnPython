#! /usr/bin/env python
from games import hangman

if __name__ == '__main__':
    game = hangman.Game('most_common_words_999.txt')
    game.start_game()
