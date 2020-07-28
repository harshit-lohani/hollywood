from typing import List, Any, Union
import random
import os
import time

def print_list(l):
  for letter in l:
    print(letter, end = " ")
  print("\n")


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear();

print("Welcome to the HollWood game, you must enter a movie or choose to get a random movie and then guess it in 8 chances\n")

movies_hollywood = open("movies_hollywood.txt").read().splitlines()
movies_bollywood = open("movies_bollywood.txt").read().splitlines()


movie = ""

choice = input("Do you want a random movie? Press y for yes, n for no: ")
if choice.upper() == "N":
    movie = input("\n\nenter the movie in / separated fashion: ")
elif choice.upper() == "Y":
  genre = input("\nPress h for (h)ollywood and b for (b)ollywood: ")
  if(genre.upper() == 'H'):
    movie = random.choice(movies_hollywood)
  if(genre.upper() == 'B'):
    movie = random.choice(movies_bollywood)
    print(movie + "1")

clear();

movie_string = movie.upper()

display_list= []
for letter in movie_string:
    if letter in "AEIOU":
        display_list.append(letter)
    elif letter == " ":
        display_list.append("/")
    else:
        display_list.append("_")

print_list(display_list)
guesses = []
index = 0
guess_limit = 8
while guess_limit > 0:

  if display_list == list(movie_string):
      print("\nYay! you guessed the movie!\n")
      break

  else:

    print("Guesses remaining: " + str(guess_limit) + "\nAlready made guesses: " + str(guesses))
    guess = input("Enter a consonant guess: ").upper()
    while guess in guesses:
      clear()
      print_list(display_list)
      print("You've already guessed that!\nAlready made guesses: " + str(guesses))
      guess = input("enter a consonant guess: ").upper()

    guesses.append(guess)

    if guess in movie_string:

      index = movie_string.find(guess)
      while index != int(len(movie_string)):

        display_list[index] = movie_string[index]
        index = movie_string.find(guess, index +1)
        if index == -1:
          if guess != movie_string[-1]:
            break
          elif display_list[index] == guess:
            break


    else:
      guess_limit -= 1

    clear()
    print_list(display_list)

if guess_limit == 0:
    print("\n***oops! you ran out of guesses, better luck next time!***")
    print("Correct answer was : " + movie_string)

else:
    print("remaining guesses: " + str(guess_limit))