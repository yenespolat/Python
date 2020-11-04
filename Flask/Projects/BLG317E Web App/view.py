from flask import Flask, render_template, current_app, abort, request, session, g, url_for, redirect
from movie import Movie
import databases


db = databases.db

def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

def profile():
    if g.user:
        return render_template('profile.html', user=session['user'])
    return redirect(url_for('login'))

def login():
    if request.method == 'POST':
        session.pop('user', None)
        username = request.form['username']
        password = request.form['password']        
        result = databases.get_user(username)
        #db.close()
        if result is not None:
            if password == result[1]:
                session['user'] = username
                return redirect(url_for('profile'))     
    return render_template('login.html')

def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        databases.add_user(username, password)
        return redirect(url_for('login'))
    return render_template('register.html')


def home():
    if g.user:
        return render_template('home.html', user=session['user'])
    return render_template('home.html')

