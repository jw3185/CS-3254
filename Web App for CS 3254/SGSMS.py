

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route("/", methods=['post', 'get'])
def someFunc():
    if request.method=='POST':
        return;
        #return render_template("printMessageRecieved.html");
                            # Email is a variable defined in the html form
                            
@app.route("/printMessageRecieved.html", methods=['post', 'get'])
def printData():
    return render_template("printMessageRecieved.html",
                           firstname=request.form["firstname"],
                           lastname=request.form["lastname"],
                           Email=request.form["Email"],
                           Password=request.form["Password"],
                           Password_CONFIRM=request.form["Password_CONFIRM"]);

if __name__ == '__main__':
    app.run("127.0.0.1",900,debug=True)#Remove when not debugging
    # "127.0.0.1" is localhost, your machine
    # app.run(host='0.0.0.0')to make public
    
