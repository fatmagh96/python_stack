from flask import flash
from mysqlconnection import connectToMySQL
DATABASE = 'dojo_survey_schema'

class Ninja:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.location = data_dict['location']
        self.language = data_dict['language']
        self.comment = data_dict['comment']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create_ninja(cls,data_dict):
        query = """ INSERT INTO dojos (name, location, language, comment)
                    VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);
                """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_info(cls,ninja_id):
        query = """
                SELECT * FROM dojos WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,{'id':ninja_id})
        print('*******************result****',result,'******************')
        return cls(result[0])
    
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['name'])<3 :
            flash("Name must be at least 3 characters.","name")
            is_valid = False
        if len(data_dict['comment']) < 3 :
            flash("Comment must be at least 3 characters.","comment")
            is_valid = False
        if not data_dict['language']:
            flash("You must choose a Language.","language")
            is_valid = False
        if not data_dict['location']:
            flash("You must choose a Location.","location")
            is_valid = False
        return is_valid
            

