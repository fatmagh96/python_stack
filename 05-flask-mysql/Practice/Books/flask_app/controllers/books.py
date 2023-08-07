from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author



@app.route('/books')
def books():
    books = Book.get_all_books()
    return render_template('books.html', books = books)

@app.route('/books/create', methods = ['POST'])
def create_book():
    Book.create_book(request.form)
    return redirect('/books')

@app.route('/books/<int:book_id>')
def show_book(book_id):
    authors = Author.get_all_authors()
    favorited = Book.get_books_favorited({'book_id':book_id})
    # fav_books = Author.get_author_favorites({'author_id':author_id})
    book = Book.get_book_by_id({'id':book_id})
    return render_template('show_book.html', book = book , authors = authors , favorited =favorited )

@app.route('/add_favorite/<int:book_id>' , methods = ['POST'])
def add_fav(book_id):
    print('😍'*5,request.form)
    data = {
        **request.form,
        'book_id':book_id
    }
    Author.add_favorite(data)
    return redirect(f'/books/{book_id}')