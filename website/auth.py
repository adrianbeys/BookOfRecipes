from website import app
from flask import  redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user
from website.forms import LoginForm, RegisterForm, ProfileForm
from website.models import DBConnection, User, UserProfile

db = DBConnection()

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for(main))
    form = RegisterForm()
    if form.validate_on_submit():
        newProfile = UserProfile()
        db.AddProfile(newProfile)
        newUser = User(email=form.emailAddress.data,
                       username=form.username.data, 
                       firstname=form.firstname.data,             
                       password=form.password1.data,
                       roleId=1, profileId = newProfile.id)
        db.AddUser(newUser)  
        db.Flush()
        login_user(newUser)
        return redirect(url_for('home_page'))
    return render_template("register.html", form=form)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    return "<p>logout</p>"


