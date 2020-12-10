import random
from GenClass import PWGenerator
passwordList = []
logInPW = []

def choice():
    ui = input("do you want to create a Password (y or n) ")
    if ui == "y":
        userPassword = input("Put your new Password: ")
        passwordList.append(userPassword)
    elif ui == "n":
        PWGenerator()

def logIn():
    username = input("What is ur username ")
    password = input("What is ur password ")

    if password in logInPW:
        choice()

def signUp():
    first = input("What is ur First name? ")
    last = input("What is ur last name ? ")
    username = input("What is ur username ")
    password = input("What is ur password ")

    print(f'''
    Your first name is {first}
    Your Last name is  {last}
    Your UserName is   {username}
    Your Password is   {password}
    ''')
    logInPW.append(password)

# def category():


# def updateData():


def PWGenerator():
    return(f'Here is your new generated password:\n{PWGenerator().createPW()}')

def pwChecker():
    passwordToCheck=input("input a password ")



print("Welcome to your Password Manager")
