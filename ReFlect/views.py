from flask import Flask, render_template, flash, redirect, url_for, request, session, logging
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from ReFlect import app, db, models, data
from ReFlect.models import User, Article
from ReFlect.data import Prompts
from ReFlect.forms import ArticleForm, RegisterForm, LoginForm
from datetime import datetime

Bootstrap(app)

prompts = Prompts()
login_manager = LoginManager(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return None

# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, Please login", 'danger')
            return redirect(url_for('login'))
    return wrap     

# Index 
@app.route('/')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Articles
@app.route('/articles')
def articles():
    # Get Articles
    articles = Article.query.filter_by(author=session['username']).all()

    if articles:
        return render_template('articles.html', articles=articles)
    else:
        msg = "No Articles Found"
        return render_template('articles.html')

    #Close Connection
    cur.close() 

# Single Article
@app.route('/article/<string:id>/')
def article(id):
    #Create cursor
    article = Article.query.filter_by(id=id).first()
    return render_template('article.html', article=article)

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('register'))
    form = RegisterForm() #create RegisterForm object, which inherits from Form object
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # Create db entry row for user
        user = User(
            name=name,
            email=email,
            username=username
        )

        user.set_password(password)

        #add user to database
        db.session.add(user)
        db.session.commit()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(
            username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            print ("INVALID")
            return redirect(url_for('login'))
        # login_user(user)
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html', title='Sign In', form=form)     

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


# Dashboard 
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Get Articles
    articles = Article.query.filter_by(author=session['username']).all()

    if articles:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = "No Articles Found"
        return render_template('dashboard.html')

@app.route('/add_article', methods=['GET','POST'])
@is_logged_in
def add_article():
    x = datetime.now()
    print("hello!")
    prompt = prompts[-1]
    form = ArticleForm(request.form)
    form.title.data = f"{x.strftime('%B')} {x.strftime('%d')}, {x.strftime('%Y')}"
    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']
        cur_prompt = prompt if form.used_prompt.data else ""

        article = Article(
            title=title,
            body=body,
            prompt=cur_prompt,
            author= session['username']
        )

       # Add article to db
        db.session.add(article)

        # Commit to DB
        db.session.commit()

        flash('Entry Created', 'success')
        
        prompts.pop()

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form, prompt=prompt)

@app.route('/edit_article/<string:id>', methods=['GET','POST'])
@is_logged_in
def edit_article(id):

    # Get article by id
    article = Article.query.filter_by(id=id).first()

    # Get form
    form = ArticleForm(request.form)

    # Populate fields
    form.title.data = article.title
    form.body.data = article.body
    print("hello!")
    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # update article fields
        article.title = title
        article.body = body

        # Commit to DB
        db.session.commit()

        flash('Entry Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)

# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
   
    # delete article 
    Article.query.filter_by(id=id).delete()

    # Commit to DB
    db.session.commit()

    flash('Entry Deleted', 'success')

    return redirect(url_for('dashboard'))
