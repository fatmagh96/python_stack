from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models import author

class Book:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.title = data_dict['title']
        self.num_of_pages = data_dict['num_of_pages']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.favorited_by = []

    @classmethod
    def create_book(cls, data_dict):
        query = """
                INSERT INTO books (title, num_of_pages) VALUES
                (%(title)s, %(num_of_pages)s);
                """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_book_by_id(cls, data_dict):
        query = """
                SELECT * FROM books WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_all_books(cls):
        query = """
                SELECT * FROM books;
                """
        result = connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for row in result:
            all_books.append(cls(row))
        return all_books
    
    @classmethod
    def get_books_favorited(cls, data_dict):
        query = """
                SELECT * FROM authors JOIN favorites ON authors.id = author_id
                JOIN books ON books.id = book_id WHERE book_id = %(book_id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(result)
        favorited_by = []
        if result:
            for row in result:
                favorited_by.append(author.Author(row))
            book = cls(result[0])
            book.favorited_by = favorited_by
            return book
        return False