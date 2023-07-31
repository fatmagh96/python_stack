from flask_app.config.mysqlconnection import connectToMySQL
from flask import request
from flask_app import DATABASE


class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls, data_dict):
        query = """
                INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return result
    @classmethod
    def get_all(cls):
        query = """ SELECT * from users ;"""
        result = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for user in result:
            all_users.append(cls(user))
        print(all_users)
        return all_users
    
    @classmethod
    def get_user_by_id(cls, user_id):
        query = """ SELECT * from users
                    WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, {'id': user_id})
        # all_users = []
        # for user in result:
        #     all_users.append(cls(user))
        # print(all_users)
        return cls(result[0])
    
    @classmethod
    def update(cls, data_dict):
        query = """
                UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s 
                WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return result
    
    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, {'id':user_id})
