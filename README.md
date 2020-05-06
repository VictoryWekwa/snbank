# snbank
A repository that contains the details of simple banking system created with Python.
This program is a simple banking system.
On run, the program present the login and tells the user to input staff login or close app to either start or close the program.
after that, if the user types in staff login, a while statement follows that reads the staff.txt file and compares it with the user input details of username and password.
if the input details is the same with the one in the stafffile.txt, login is successful and the user is presented with options to either creat new bank account, check account details or log out.
i used 1,2 and 3 to accept the user's input.
if the user inputs 1, the fill in their details and i show them thir account number which i generated with the ramdom and randrange function.
If user selects 2, they input their account details and the program print thir account details which was saved in the customer.txt file using the append method of the file system.
the user is presented with option again and if they enter 3, the program end. i used the exit function to terminate the program.
i created a user.sessionfile on successful login using the write method, that is open('user_SessionFile.txt','w') on the user enter option 3, my session file is deleted permanently. I used the os.unlink function to delete my session file.

the last line of my program is covers if the user decides to enter close app, which prints goodbye and end.
