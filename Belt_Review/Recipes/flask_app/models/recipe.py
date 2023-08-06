from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import flash




class Recipe:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.name = data_dict['name']
        self.description = data_dict['description']
        self.instructions = data_dict['instructions']
        self.date = data_dict['date']
        self.under_30 = data_dict['under_30']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster = ""

    @classmethod
    def create_recipe(cls, data_dict):
        query = """
                INSERT INTO recipes (user_id,name,description,instructions,date,under_30)
                VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,%(date)s,%(under_30)s);
                """
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def update_recipe(cls, data_dict):
        query = """
                UPDATE recipes 
                SET name = %(name)s, description = %(description)s,
                            instructions = %(instructions)s , date = %(date)s,
                            under_30 = %(under_30)s
                WHERE id = %(id)s   ;
                """
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_recipe_by_id(cls,data_dict):
        query = """
                    SELECT * FROM recipes 
                    JOIN users ON recipes.user_id = users.id 
                    WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        recipe = cls(result[0])
        recipe.poster = result[0]['first_name']
        return recipe
    
    @classmethod
    def destroy(cls, data_dict):
        query = """
                DELETE FROM recipes WHERE id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for row in result:
            recipe = cls(row)
            recipe.poster = row['first_name']
            all_recipes.append(recipe)
        return all_recipes
    

    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['name']) < 3:
            flash("name too short!","name")
            is_valid = False
        if len(data_dict['description']) < 3:
            flash("description too short!","description")
            is_valid = False
        if len(data_dict['instructions']) < 3:
            flash("instructions too short!","instructions")
            is_valid = False
        if len(data_dict['date']) < 1:
            flash("date required!","date")
            is_valid = False

        return is_valid
