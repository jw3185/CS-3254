
This is the documentation for Some Generic Social Media Site (SGSMS)

(2/24/2016)
-------------------------------------------------
imgs folder not used yet for anything           |
-------------------------------------------------
templates folder contains four html files

One is for the main page called index, this page is mostly made up of forms
and two submit buttons and allows users to either login or create an account.

signUp.html is used when someone successfully creates a new account on the site, 
it displays the information entered into the forms and states that the account 
was created successfully

userHome.html is used to represent what the user sees when they login in 
(currently not functional, its static and generic for all users)

login.html links to userHome if login was successful
----------------------------------------------------------------------------------

styleForMainIndex.css, not used for anything yet may or may not be used in future
along with additional css files

----------------------------------------------------------------------------------
SGSMS, Python file for the server.

Defines a user class, creates a dictionary for users, handles requests

/////////////////////////////////////////////////////////////////////////////////////////
Features to be Added:

 1. Make userHome actually work
 2. Make it possible for users to delete their accounts if they want to
 3. Make it possible for users to send a message/post something
 4. Make it possible for users to specify which other users have posts
    that they find interesting
 5. Add Style with .css files(Maybe...)
/////////////////////////////////////////////////////////////////////////////////////////