#
#  Created by Jeremy Wu (netID: jw3185)
#  for CS 3254 Introduction to Parallel and Distributed Systems
#
#  This is the Python file for the server for my Web application
#


from flask import Flask, render_template, request

users = {} # key-value: ["email":"user_data", "etc":"etc",...]

class user:

    def __init__(self, email,name, password, friends=[], posts=[],
                 extraAttr1="None", extraAttr2="None"):
        self.name = name;
        self.email = email;
        self.password = password; #hash?
    
    def addPost(self, post):
        if post not in posts:
            posts += post;

    def addFriend(self,friend):
        if friend not in friends:
            friends+=friend;
        
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")
                           
@app.route("/signUp.html", methods=['post', 'get'])
def signUpFunc():

    if request.form["Email"] in users:

        return "That email has already been used to register an account"

    elif request.form["Password"]!=request.form["Password_CONFIRM"]:

        return "The password and the password confirmation does not match"

    else:

        name = (request.form["firstname"] + " " + request.form["lastname"])
        email = request.form["Email"]
        password = request.form["Password"] # make more secure later

        new_user = user(email,name,password)
        users[email]= new_user
        
        return render_template("signUp.html",
                           firstname=request.form["firstname"],
                           lastname=request.form["lastname"],
                           Email=request.form["Email"],
                           Password=request.form["Password"],
                           Password_CONFIRM=request.form["Password_CONFIRM"]);
          

@app.route("/login.html", methods=["post"])
def login():

    if request.form["Email"] not in users:

        return "<p>That e-mail is not registered to an account on this site</p>"

    elif request.form["Email"] in users:

        user_data = users.get(request.form["Email"]);

        if request.form["Password"] != user_data.password:
            return "<p>The password you entered was incorrect</p>";

        elif request.form["Password"] == user_data.password:
            return render_template("userHome.html");

        #userHome is generic and static for all users currently,
        #aka its not functional at all its just a mockup
           
if __name__ == '__main__':
    app.run("127.0.0.1",900,debug=True)#Remove when not debugging
    # "127.0.0.1" is localhost, your machine,(app.run(host='0.0.0.0')to make public)

    
