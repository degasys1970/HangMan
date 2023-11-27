# Hangman game
from os import makedirs
import random

def selected_a_word():
  words = ['working', 'hard', 'makes', 'things', 'easier', 'programming', 'computer']
  word = words[random.randint(0, len(words) - 1)]
  return word

def get_blank_word(word):
  blank_word = ''
  for i in range(len(word)):
    blank_word += '_'
  return blank_word

def word_hangman(word, so_far, letter, try_left):
  bad_try = True
  for i in range(len(word)):
    if word[i] == letter:
      so_far = so_far[:i] + letter + so_far[i+1:]
      bad_try = False
  if bad_try:
    try_left -= 1
    print('Wrong try left: ', try_left)
  print('So far you left: ', so_far)
  if word == so_far:
    print('You win!')
  elif try_left == 0:
    print('You lose!')
  else:
    next_letter = input('Next letter: ')
    word_hangman(word, so_far, next_letter, try_left)

# play the game
word = selected_a_word()
blank_word = get_blank_word(word)
word_hangman(word, blank_word, word[0] , 10)