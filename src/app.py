from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User


from flask import Flask, render_template, request, session, make_response

__author__= 'rtaylor'

from flask import Flask

app = Flask(__name__)

#'/' sympolizes and empty route and means will route to www.mysite.com/api/ the last
#forward slash is the endpoint

@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/login')
#now define an method that will execute when we access that endpoint
def login_template():
    return render_template('login.html')

@app.route('/register')
def register_template():
    return render_template('register.html')

#now we have to insert this if statement as a requirement to run the app.
if __name__ == '__main__':
    #if you need to change the port from 5000 to something else use the port arg
    #I will just to have an example.
    app.run(port=4995)



