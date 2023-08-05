from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls, data_dict):
        query = """ INSERT INTO users (email) VALUES (%(email)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for row in result:
            all_users.append(cls(row))
        return all_users
    
    @classmethod
    def get_one_by_id(cls, data_dict):
        query = "SELECT * FROM users WHERE id = %(id)s ;"
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return cls(result[0])
    
    @classmethod
    def destroy(cls, data_dict):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data_dict)

    @staticmethod
    def validate(user):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,user)
        # if result != ():
        if len(result)>0:
            flash("Email already Taken !!")
            is_valid = False
        # all_users = User.get_all()
        # for one_user in all_users:
        #     if user['email'] == one_user.email:
        #         flash("Email already Taken !!")
        #         is_valid = False
        return is_valid
