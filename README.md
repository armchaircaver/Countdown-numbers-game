# Countdown-numbers-game
Python3 script to generate all solutions to a countdown numbers game. 

Countdown is a game show, described here: https://en.wikipedia.org/wiki/Countdown_(game_show)

The program produces all the solutions to a numbers game, and analyses some statistics relating to the solutions generated

The program eliminates most duplicate entries, and eliminates frivolous solutions that invove multipying or deviding by one, or adding or suptracting zero.

A small number of duplicates slip through when there are long strings of additions or multiplications, e.g. a+b+c+d and b+a+c+d might both appear in solutions.
