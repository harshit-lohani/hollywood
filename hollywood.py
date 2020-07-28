from typing import List, Any, Union
import random
print("\n\n Welcome to the HollWood game, you must enter a movie or choose to get a random movie \n and then guess it in 8 chances \n\n")

movies = open("movies.txt").readlines()

choice = input("\ndo you want a random movie? press y for yes, n for no: ")
if choice.upper() == "N":
    movie = input("\n\nenter the movie in / separated fashion: \n")
if choice.upper() == "Y":
  
    movie = random.choice(movies)

movie_string = movie.upper()
# print(movie_string)
display_list= []
for letter in movie_string:
    if letter in "AEIOU":
        display_list.append(letter)
    elif letter in "/":
        display_list.append("/")
    else:
        display_list.append("_")

print("\n\n        " + str(display_list) + "\n")
guesses = []
index = 0
guess_limit = 8
while guess_limit > 0:
    if display_list == list(movie_string):
        print("\n\n yay! you guessed the movie! \n")
        break
    else:

        print("guesses remaining: " + str(guess_limit) + "\nalready made guesses: " + str(guesses))
        guess = input("enter a consonant guess: ").upper()
        while guess in guesses:
            print("you've already guessed that! \n" + "\nalready made guesses: " + str(guesses))
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
        print("\n\n        " + str(display_list) + "\n")
if guess_limit == 0:
    print(" \n\n ***oops! you ran out of guesses, better luck next time!*** \n")
else:
    print("remaining guesses: " + str(guess_limit))