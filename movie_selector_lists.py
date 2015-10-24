#!/usr/bin/env python 2.7

"""This is a program for When you are bored & don't know what movie to watch"""

from __future__ import print_function
import random, sys, pickle
import os.path

available_movie_list = ["Buffy", "Angel", "Willow", "Giles", "Spike"]
played_movie_list = ["Narnia"]
available_movie_count = len(available_movie_list)
played_movie_count = len(played_movie_list)

def solicit_user_action():
    print('Action List')
    print('1.  Add \n2.  Pick My Own \n3.  Random Choice \n4.  Delete \n5.  View Movies \n6.  View Played \n7.  Exit\n')
    user_selection = input('What would you like to do? \n').lower()
    print('\n')

    if (user_selection == 'add') or (user_selection == "1"):
        add_movie_to_available_movie_list(available_movie_list, available_movie_count)
    elif (user_selection =='pick') or (user_selection == "2"):
        user_pick_movie(available_movie_list, available_movie_count)
    elif (user_selection == 'random') or (user_selection == "3"):
        choose_random_movie(available_movie_list, available_movie_count, played_movie_list, played_movie_count)
    elif (user_selection == 'delete') or (user_selection == "4"):
        delete_movie_from_available_movie_list()
    elif (user_selection == 'view movies') or (user_selection == '5'):
        print_available_movie_list()
    elif (user_selection == 'view played') or (user_selection == '6'):
        print_played_movie_list()
    elif (user_selection == 'quit') or (user_selection == "exit") or (user_selection == "7"):
        sys.exit()

def choose_random_movie(available_movie_list, available_movie_count, played_movie_list, played_movie_count):
    random_choice = int(random.randint(0, available_movie_count-1))
    print("Your Movie Selection is: ", available_movie_list[random_choice]) 
    movie_to_transfer = available_movie_list[random_choice]
    available_movie_list.pop(random_choice) 
    available_movie_count -= 1
    copy_to_played_movie_list(movie_to_transfer)
    played_movie_count += 1

def user_pick_movie(available_movie_list, available_movie_count):
    print_available_movie_list()
    user_selection_string = input("What Movie would you like to watch? \n").title()
    if user_selection_string in available_movie_list:
        user_selection_index = available_movie_list.index(user_selection_string) #Note: This may get buggy if multiple elements have similar names & user doesn't enter full title
        user_selected_movie = available_movie_list[user_selection_index]
        print('\nYou chose: ', user_selected_movie, '\nEnjoy!! \n')
    elif user_selection_string == "Menu":
        return
    else:
        print("\nThat's not a valid movie.  \nEnter a Movie from the list, or Type 'Menu' to return to the Main Menu")
        user_pick_movie(available_movie_list, available_movie_count)


    
def add_movie_to_available_movie_list(available_movie_list, available_movie_count):
    print("Ok - Let's add a Movie! \n")
    new_movie_to_add = input('Movie Name? ').title()
    available_movie_list.append(new_movie_to_add)
    available_movie_count +=1
    print_available_movie_list()

def print_available_movie_list():
    print("Available Movie List: \n")
    for num in range(len(available_movie_list)):
        print(available_movie_list[num])
    print('\n')

def delete_movie_from_available_movie_list():
    print_available_movie_list()
    movie_to_delete = input('What would you like to delete? \n').title()
    if movie_to_delete.title() in available_movie_list:
        available_movie_list.remove(movie_to_delete)
    elif movie_to_delete == "Menu":
        return
    else:
        print("\nThat movie's not on the list.  \nEnter a Movie from the List, or Type 'Menu' to return to the Main Menu")
        delete_movie_from_available_movie_list()
    print_available_movie_list()

def add_movie_to_played_list():
    played_movie_to_add = input('Movie Name? ').title()
    played_movie_list.append(played_movie_to_add)
    print(played_movie_list, '\n')

def copy_to_played_movie_list(movie_name):
    played_movie_list.append(movie_name)

def print_played_movie_list():
    print('Played Movie List: \n')
    for num in range(len(played_movie_list)):
        print(played_movie_list[num])
    print('\n')


if __name__ == "__main__":

    print('Available Movie List: \n')
    for num in range(len(available_movie_list)):
        print(available_movie_list[num])
    print("\n")

    run = True
    while run:
        print('Welcome to the Movie Selector \n')
        solicit_user_action()

