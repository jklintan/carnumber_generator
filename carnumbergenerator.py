#Josefine Klintberg, python project
#Generating and control of carnumbers

import random
import string
from bintree import*

#Files & Definitions
letters = 'ABCDEFGHJKLMNOPRSTUWXYZ'
numbs = '0123456789'
bannedwords = open("bannedwordcombinations.txt", encoding='utf-8').read().split()
banned = set(bannedwords)

#Main menu
def startmenu():
    print("Welcome to the carnumber control (Swedish version) ")
    user = int(input("What can I help you with? \n1. Generate carnumber 2. Control carnumber 3. Exit \n"))
    if user == 1:
        generator()
    elif user == 2:
        print("How do you want to control your carnumbers? ")
        user_next = int(input("1. By input 2. From file: \n"))
        if user_next == 1:
            user_number = input(str("Write the carnumber you want to control \n(with space in between the numbers and letters) \n"))
            print(textcontrol(user_number))
        elif user_next == 2:
            filecontrol()
        else:
            error()
    elif user == 3:
        exit()
    else:
        error()
            
#Generation of carnumbers
def generator():
    num_gen = int(input("How many carnumber do you wish to generate? "))
    name_f = input("To which file do you want to write the numbers? ")
    file = open(name_f, 'w')
    tree = bintree()
    while num_gen > 0:
        let = ''.join([random.choice(letters) for n in range(3)])
        numb = ''.join([random.choice(numbs) for n in range(3)])
        car_number = let +' ' + numb
        #Control if banned
        if let not in banned:
            if tree.put(car_number) == True: #Check so no multiples
                file.write(car_number+'\n')
                tree.put(car_number)
                num_gen -= 1
            else:
                num_gen += 0
        else:
            num_gen +=0 
    file.close()
    print("Your carnumbers are now in the file " + name_f)

#Control of single carnumber
def textcontrol(user_number):
    the_letters = user_number[:3]
    if len(user_number)!=7 or str(user_number[4])==True or int(user_number[4])==True or str(user_number[:3])==False or int(user_number[-3:])==False:
        return "Not a valid carnumber"
    else:
        if the_letters in banned:
            return "Banned combination of carnumber"
        else:
            return "OK"

#Controls of carnumbers in file, and generation of file
def filecontrol():
    user_file = input("Which file do you want to read in carnumbers from? ")
    the_numbers = open(user_file, 'r', encoding='utf-8')
    result = input("Which file do you want to get the results in? ")
    new_file = open(result, 'w', encoding='utf-8')
    for word in the_numbers.read().split('\n'): #Read in numbers one at a time
        text_control = textcontrol(word)
        new_file.write(word + ' ' + text_control + '\n')
    new_file.close()
    print("Control is finished and can be seen in the file " +result)

#Errorfunction
def error():
    print("Fel inmatning. Omstart sker...")
    wait = input("Tryck enter för att fortsätta \n")
    startmenu()
