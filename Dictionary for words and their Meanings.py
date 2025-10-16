def addword():
    word = input("Enter a word: ")
    meaning = input("Enter the meaning: ")
    dictionary[word] = meaning
    print("New word added!\n")
    mainfun()

def show_meaning():
    checkword = input("Enter the word to find the meaning: ")
    if checkword in dictionary:
        print("Meaning:", dictionary[checkword])
    else:
        print("Word not found!")
    print()
    mainfun()

def show_dictionary():
    if dictionary:
        print("Current Dictionary:", dictionary)
    else:
        print("Dictionary is empty.")
    print()
    mainfun()

dictionary = {}

def mainfun():
    print("***** Dictionary *****")
    print("choice--1 : Add a Word in Dictionary")
    print("choice--2 : Show me the meaning")
    print("choice--3 : Show all words")
    print("choice--4 : Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        return mainfun()

    if choice == 1:
        addword()
    elif choice == 2:
        show_meaning()
    elif choice == 3:
        show_dictionary()
    elif choice == 4:
        print("Good Bye! Please visit again!!!")
    else:
        print("##### Invalid input #####\n")
        mainfun()

mainfun()
