from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from flask import flash

class User:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # ---------------- CRUD QUERIES = classmethods --------------------

    @classmethod
    def create(cls, data_dict):
        query = """ 
                    INSERT INTO users (first_name, last_name, email, password) 
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        return connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len(data_dict['first_name'])<2:
            print("First name too short....")
            flash("First name too short....")
            is_valid = False
        if len(data_dict['last_name'])<2:
            print("last name too short....")
            flash("last name too short....")
            is_valid = False
        if len(data_dict['password'])<8:
            print("password too short....")
            flash("password too short....")
            is_valid = False
        elif data_dict['password'] != data_dict['confirm_password']:
            print('confirm password is different from password')
            flash('confirm password is different from password')
            is_valid = False
        
        return is_valid
        