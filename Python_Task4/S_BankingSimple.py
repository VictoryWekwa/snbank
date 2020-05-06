# A  program for simple banking system file type
##

from random import randrange
import os

login = input("Welcome, enter staff login to continue or close app to exit: ")
# The program starts after accepting the input login option
while login == "staff login":
    staff_details = open('staffFile.txt', 'r')
    user_name = input('Enter your username: ')
    user_password = input('Enter your password: ')
    username = staff_details.read()
    password = staff_details.read()
    if user_name == username and user_password == password:
        print('login successful')
        successful_login = True
    else:
        print('Incorrect details! Enter correct details to continue')
    staff_details.close()
# if login is successful create the session file and present the options
    while True:
        session_details = open('user_SessionFile.txt', 'w')
        option = input(""" select any of the following to continue:
        Create new account, Check account details, logout.Enter 1, 2 or 3: """)
        while option == '1':
            Account_name = input('Enter your account name: ')
            opening_balance = input('please enter your opening balance: ')
            account_type = input('Enter your account type: ')
            account_email = input('Your account email please: ')
            generated_account_number = [randrange(0, 9, 1) for _ in range(10)]
            print('Your account number is', generated_account_number)
            customer_details = open('Customer.txt', 'a')
            customer_details.write('\n' + Account_name + ',' + opening_balance + ',' + account_type + ',' +
                                   account_email)
            option = input(""" select any of the following to continue:
                    Create new account, Check account details, logout.Enter 1, 2 or 3: """)

        while option == '2':
            account_number = int(input('Enter your account number: '))
            customer_details = open('Customer.txt', 'r')
            account_details = customer_details.read()
            print(account_details)
            customer_details.close()
            option = input(""" select any of the following to continue:
                        Create new account, Check account details, logout.Enter 1, 2 or 3: """)
        while option == '3':
            login_successful = False
            session_details.close()
            os.unlink('user_SessionFile.txt')
            exit()

while login == 'close app':
    print('Goodbye')
    break












