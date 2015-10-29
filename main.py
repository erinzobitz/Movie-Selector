#!/usr/bin/python

"""This is a program for When you are bored & don't know what movie to watch"""

import sqlite3 as lite
import random, sys, pickle
import os.path

con = lite.connect('movie_list_db.sqlite')

available_movie_list = ["Buffy", "Angel", "Willow", "Giles", "Spike"]
played_movie_list = ["Narnia"]
available_movie_count = len(available_movie_list)
played_movie_count = len(played_movie_list)

def solicit_user_action():
    """Gets the User's Main Menu Choice"""
    print('Action List')
    print('1.  Add \n2.  Pick My Own \n3.  Random Choice \n4.  Delete Move \n5.  Delete List \n6.  View Movies \n7.  View Played \n8.  Exit\n')
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
    elif (user_selection == 'delete list') or (user_selection == '5'):
        delete_movie_list()
    elif (user_selection == 'view movies') or (user_selection == '6'):
        print_available_movie_list()
    elif (user_selection == 'view played') or (user_selection == '7'):
        print_played_movie_list()
    elif (user_selection == 'quit') or (user_selection == "exit") or (user_selection == "8"):
        sys.exit()

def choose_random_movie(available_movie_list, available_movie_count, played_movie_list, played_movie_count):
    """The Program chooses a Random Movie for the User"""
    random_choice = int(random.randint(0, available_movie_count-1))
    print("Your Movie Selection is: ", available_movie_list[random_choice]) 
    movie_to_transfer = available_movie_list[random_choice]
    available_movie_list.pop(random_choice) 
    available_movie_count -= 1
    copy_to_played_movie_list(movie_to_transfer)
    played_movie_count += 1

def user_pick_movie(available_movie_list, available_movie_count):
    """Lets User Pick A Movie From Available Movie List"""
    #This should probably allow the user which list to choose
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
    """Adds a Movie to the Available Movie List"""
    print("Ok - Let's add a Movie! \n")
    new_movie_to_add = input('Movie Name? ')
    new_movie_temp = (new_movie_to_add, ) #*** THIS LINE IS NECESSARY SO THAT IT GOES INTO THE INSERT STATEMENT AS A TUPLE
    print("Adding ", new_movie_to_add)
    con.execute("INSERT INTO AVAILABLE_MOVIE_LIST (MOVIE_NAME) \
    VALUES (?)", (new_movie_temp)); #NO IDEA WHY IT DOESN'T WORK TO DO THE TUPLE HERE :( :( :( )))

    con.commit()
    print("Movie Added \n")

def print_available_movie_list():
    """Prints the Available Movie List for the User to See"""
    cur.execute("SELECT * FROM AVAILABLE_MOVIE_LIST")
    for row in cur:
        print("Movie Number: ", row[0])
        print("Movie Name: ", row[1])
        print("")

def delete_movie_from_available_movie_list():
    """Deletes a Single Movie from the available Movie List"""
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

def delete_movie_list():
    """Will allow the user to delete any or all of the Movie Lists"""
    #This needs to be implemented so the user can choose which Lists to delete.  For now, it will just delete all lists.
    cur.execute("DELETE FROM AVAILABLE_MOVIE_LIST WHERE ID IN (SELECT ID FROM AVAILABLE_MOVIE_LIST)")
    con.commit()
    print("")
    print("Entire List Deleted")

def add_movie_to_played_list():
    """Transfers a User Inputted Movie to the Played Movies List"""
    played_movie_to_add = input('Movie Name? ').title()
    played_movie_list.append(played_movie_to_add)
    print(played_movie_list, '\n')

def copy_to_played_movie_list(movie_name):
    """Helper Function that Transfers a Selected Movie to the Played Movies List"""
    played_movie_list.append(movie_name)

def print_played_movie_list():
    print('Played Movie List: \n')
    for num in range(len(played_movie_list)):
        print(played_movie_list[num])
    print('\n')


if __name__ == "__main__":
    cur = con.cursor()

    con.execute('''CREATE TABLE IF NOT EXISTS AVAILABLE_MOVIE_LIST (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_NAME TEXT NOT NULL);''')
    print("Create Sucess")

    print('Available Movie List: \n')
    cur.execute("SELECT * FROM AVAILABLE_MOVIE_LIST")
    print_available_movie_list()
    # for row in cur:
    #     print("Movie Number: ", row[0])
    #     print("Movie Name: ", row[1])
    #     print("")


    run = True
    while run:
        print('Welcome to the Movie Selector \n')
        solicit_user_action()

