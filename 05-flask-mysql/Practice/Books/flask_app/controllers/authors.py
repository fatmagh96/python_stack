from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all_authors()
    return render_template('authors.html', authors = authors)

@app.route('/authors/create', methods = ['POST'])
def create_author():
    Author.create_author(request.form)
    return redirect('/authors')

@app.route('/authors/<int:author_id>')
def show_author(author_id):
    books = Book.get_all_books()
    fav_books = Author.get_author_favorites({'author_id':author_id})
    print(fav_books.favorite_books)
    author = Author.get_author_by_id({'id':author_id})
    return render_template('show_author.html', books = books , author = author , fav_books =fav_books )

@app.route('/add_favorite/<int:author_id>' , methods = ['POST'])
def add_fav_book(author_id):
    print('😍'*5,request.form)
    data = {
        **request.form,
        'author_id':author_id
    }
    Author.add_favorite(data)
    return redirect(f'/authors/{author_id}')

# redirect(f'/recipes/edit/{recipe_id}')