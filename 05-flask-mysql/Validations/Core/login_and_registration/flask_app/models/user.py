from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pw_regex = re.compile("^(?=.*?[A-Z])(?=.*?[0-9]).{8,}$")


bcrypt = Bcrypt(app)

class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.birthday = data_dict['birthday']
        self.gender = data_dict['gender']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create_user(cls, data_dict):
        query = """
                INSERT INTO users (first_name,last_name,email,password,birthday,gender)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(birthday)s,%(gender)s);
                """
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_user_by_id(cls,data_dict):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return cls(result[0])
    
    @classmethod
    def get_user_by_email(cls,data_dict):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        if len(result)>0:
            return cls(result[0])
        return False
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for row in result:
            all_users.append(cls(row))
        return all_users
    
    @staticmethod
    def login_validation(data_dict):
        is_valid = True
        user = User.get_user_by_email(data_dict)
        if not user:
            flash("Email or Password invalid !!",'login')
            is_valid = False
        elif not bcrypt.check_password_hash(user.password, data_dict['password']):
            flash("Email or Password invalid !!",'login')
            is_valid = False
        return is_valid

    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['first_name']) < 2:
            flash("First name too short!","first_name")
            is_valid = False
        if len(data_dict['last_name']) < 2:
            flash("Last name too short!","last_name")
            is_valid = False

        # query = "SELECT * FROM users WHERE email = %(email)s;"
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        user = User.get_user_by_email(data_dict)
        
        if not EMAIL_REGEX.match(data_dict['email']):
            flash("Invalid Email!!!",'email')
            is_valid=False
        # if len(result)>0:
        if user:
            flash("Email already taken!!","email")
            is_valid = False

        # if len(data_dict['password'])<8:
        #     flash("Password must be at least 8 characters", "password")
        #     is_valid = False
        if not pw_regex.match(data_dict['password']):
            flash("Password must be at least 8 characters and contain at least one Uppercase and one number", "password")
            is_valid = False
        elif data_dict['password'] != data_dict['confirm_password']:
            flash("Password and Confirm password dont match","password")
            is_valid = False

        if len(data_dict['birthday'])<1:
            flash("Please enter your date of birth","birthday")
            is_valid = False
        elif data_dict['birthday'] < '1960-12-12':
            flash("Too old! Sorry ..","birthday")
            is_valid = False

        return is_valid
