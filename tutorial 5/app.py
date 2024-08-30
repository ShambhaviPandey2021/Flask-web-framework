#from flask import Flask

# WSGI application

#app = Flask(__name__)

#@app.route('/') #Decorator

#def world():
#   return "Welcome to my first flask tutorial!.Please  Please Learn with me ."

#@app.route('/members')

#def members():
#    return "Welcome to my first flask tutorial!."



#if __name__== '__main__':
#    app.run(debug = True)
    
    
    
    
## Building URL Dynamically
## Variable Rules and URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')

def welcome():
    return "Welcome to my first flask tutorial!"

@app.route('/success/<int:score>')

def success(score):
    return "The person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h1>The result  is failed.</h1></body></html>"


@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score= marks))

if __name__=='__main__':
    app.run(debug = True)