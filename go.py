#!/usr/bin/env python3

import sys
import os

def read():
    if len(sys.argv) != 2:
        print("Error: invalid arguments")
        help()
        return
    target = sys.argv[1]    
    reader = open('bookmarks.txt', 'r').readlines()
    for i in range(len(reader)):
        current_string_list = reader[i].split()
        match = current_string_list[0]
        if match == target:
            os.system("open " + current_string_list[1])
            return

    print("No match found. Type 'go add [shortcut] [link]' to add a new bookmark")
    

def add():
    if len(sys.argv) < 4:
        print("Error: not enough arguments")
        help()
        return
    adder = open('bookmarks.txt', 'a')
    addMe = sys.argv[2] + " " + sys.argv[3] + '\n'
    adder.write(addMe)
    print("Added bookmark " + addMe)

def help():
    print("Usage:")
    print("     go [option] [alias] <link if option='-a'>")
    print("Options:")
    print("     [alias] -- opens the pre-saved shortcut alias in the default web browser")
    print("     -a [alias] [link] -- adds a link associated with the alias to be used later")
    print("     -h -- prints this help message")
    print("     -l -- displays a list of all saved aliases and their corresponding links")
    print("     -r [alias] -- removes the link associated with the alias")

def list():
    print()
    print ("===============SAVED LINKS================")
    print()
    reader = open('bookmarks.txt', 'r').readlines()
    for i in range(len(reader)):
        print(reader[i])
    print("===========================================")


if len(sys.argv) > 1 and (sys.argv[1] == '-a' or sys.argv[1] == '--add'):
    add()
elif sys.argv[1] == "-h":
    help()
elif sys.argv[1] == "-l":
    list()
elif len(sys.argv) == 2:
    read()
else:
    print("Error: invalid arguments")
    help()


# © Aiden McCormack, 2023. All rights reserved.
