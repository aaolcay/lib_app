#!/usr/bin/python

# /*
#  * Copyright (C) 2020  Abdullah Azzam Olcay
#  * University of Southampton
#  * Lınkedin: https://tr.linkedin.com/in/abdullah-azzam-olcay-613453183
#  *
#  * Please do not remove this header.
#  * */
import os
import time

book_list = list()

menu = """
[1] Add books
[2] Remove a book or take a book
[3] List of all books
[Q] Quit/Exit
"""

def add_book(book:tuple,book_list:list):
    book_list.append(book)
    print("The book is added.\n")

def control(book:tuple,book_list:list): # Is the book added or in book_list?
    if book in book_list:
        return True
    else:
        return False

def remove_book(book:tuple,book_list:list):
    book_list.remove(book)
    print("The book is removed/taked.\n")

def print_list(book_list:list):
    for i in book_list:
        print("Book Name: {} -----> Book Author: {}".format(i[0],i[1]))


while True:
    os.system("clear") # You should use cls for Windows. It clear the terminal window
    print(menu)
    selection = str(input("Select you want to do:\n"))

    if selection == "1":
        x = int(input("How many book do you want to enter:\n"))
        for i in range(x):
            book_name = input("Enter the book name:\n")
            book_author = input("Enter the author of the book:\n")
            book = (book_name,book_author)
            add_book(book,book_list)
        print("Please wait for a second, you will go to main menu\n")
        time.sleep(3)

    elif selection == "2":
        y = int(input("How many books do you want to take/remove:\n"))
        for i in range(y):
            print("Which book do you want to remove:\n")
            removed_book_name = input("Enter the name of book:\n")
            removed_book_author = input("Enter the author of the book:\n")
            removed_book = (removed_book_name,removed_book_author)
            control_statement = control(removed_book,book_list)
            if control_statement == True:
                    remove_book(removed_book,book_list)
            else:
                    print("This book you want to remove is absent in the list")
        print("Please wait for a second, you will go to main menu\n")
        time.sleep(3)


    elif selection == "3":
        print_list(book_list)

    elif selection == "q" or selection == "Q":
        print("The books to enjoy...\n")
        quit()
    else:
        print("Your selection absent on menu...")
