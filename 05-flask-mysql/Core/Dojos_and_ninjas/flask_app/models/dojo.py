from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models.ninja import Ninja 


class Dojo:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        all_dojos = []
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        for dojo in result:
            all_dojos.append(cls(dojo))
        return all_dojos
    
    @classmethod
    def get_all_ninjas_in_dojo(cls, dojo_id):
        query = """
                SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, {'id':dojo_id})
        print("***********",result, "****************")
        if result:
            dojo = Dojo(result[0])
            # all_ninjas = []
            for ninja in result:
                ninja_data = {
                    'id':ninja['ninjas.id'],
                    'dojo_id':ninja['dojo_id'],
                    'first_name': ninja['first_name'],
                    'last_name': ninja['last_name'],
                    'age': ninja['age'],
                    'created_at': ninja['ninjas.created_at'],
                    'updated_at': ninja['ninjas.updated_at'],
                }
                dojo.ninjas.append(Ninja(ninja_data))
                # all_ninjas.append(Ninja(ninja_data))
            print("++++++++++++++++++++",dojo.ninjas,"++++++++++++++++++++++++++++++")
            return dojo
        return False
    
    @classmethod
    def create_dojo(cls,data_dict):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    

