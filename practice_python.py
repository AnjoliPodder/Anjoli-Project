'''
Worked examples from http://www.practicepython.org/
Written by Anjoli Podder
12/2016
'''

'''
#1
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
tells them the year that they will turn 100 years old.
'''

import datetime

def year_100():
    name = input("Please enter your name:")
    age = input("Please enter your age:")
    year_at_100 = 100 - int(age) + datetime.datetime.now().year
    print("Hi,",name, "The year when you are 100 will be", year_at_100)

'''
#2
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''

def less_than_5(input_list):
    return [x for x in input_list if x < 5]

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def divisors(num):
    div_list = [1]
    for x in range(2,int(num/2)+1):
        if num%x == 0:
            div_list.append(x)
    div_list.append(num)
    return div_list

'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
'''

def common(list1, list2):
    com = []
    if len(list2) < len(list1):
        list2, list1 = list1, list2
    for el in list1:
        if el in list2 and not(el in com):
            com.append(el)
    return com


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common(a, b))

'''
#8
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

def rps():
    print("Welcome to the game! Your move must be rock, paper or scissors.")
    valid_moves = ["rock", "paper", "scissors"]
    valid1 = True
    valid2 = True
    pl1 = ""
    pl2 = ""
    while valid1 == True:
        pl1 = input("Please enter your move, Player 1").lower()
        if not(pl1 in valid_moves):
            print("That was not a valid move. Try again.")
        else:
            valid1 = False
    while valid2 == True:
        pl2 = input("Please enter your move, Player 2").lower()
        if not(pl2 in valid_moves):
            print("That was not a valid move. Try again.")
        else:
            valid2 = False
    if pl1 == pl2:
        print("You both chose", pl1,". It's a tie!")
    elif (pl1, pl2) == ("rock", "paper"):
        print("Player 2 Wins! Paper beats Rock")
    elif (pl1, pl2) == ("rock", "scissors"):
        print("Player 1 Wins! Rock beats Scissors")
    elif (pl1, pl2) == ("paper", "scissors"):
        print("Player 2 Wins! Scissors beats Paper")
    elif (pl1, pl2) == ("paper", "rock"):
        print("Player 1 Wins! Paper beats Rock")
    elif (pl1, pl2) == ("scissors", "paper"):
        print("Player 1 Wins! Scissors beats Paper")
    elif (pl1, pl2) == ("scissors", "rock"):
        print("Player 2 Wins! Rock beats Paper")
    again = input("Do you want to play again? (Y/N)").lower()
    if again == "y":
        rps()
    else:
        print("Thanks for playing!")
        pass



