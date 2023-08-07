from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models.book import Book

class Author:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.favorite_books = []

    @classmethod
    def create_author(cls, data_dict):
        query = """
                INSERT INTO authors (name) VALUES
                (%(name)s);
                """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_author_by_id(cls, data_dict):
        query = """
                SELECT * FROM authors WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_all_authors(cls):
        query = """
                SELECT * FROM authors;
                """
        result = connectToMySQL(DATABASE).query_db(query)
        print("++++++++0",result,"+++++++++++++")
        all_authors = []
        for row in result:
            all_authors.append(cls(row))
        return all_authors
    
    @classmethod
    def add_favorite(cls, data_dict):
        query = """
                INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s)
                """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_author_favorites(cls, data_dict):
        query = """
                SELECT * FROM authors JOIN favorites ON authors.id = author_id
                JOIN books ON books.id = book_id WHERE author_id = %(author_id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(result)
        fav_books = []
        if result:
            for row in result:
                data = {
                    **row, 
                    'created_at':row['books.created_at'],
                    'updated_at':row['books.updated_at']
                }
                fav_books.append(Book(data))
            author = cls(result[0])
            author.favorite_books = fav_books
            return author
        return False