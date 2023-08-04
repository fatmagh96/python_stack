from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask_app.models.dojo import Dojo



class Ninja:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.dojo_id = data_dict['dojo_id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
         

    # @classmethod
    # def get_all_ninjas_in_dojo(cls, dojo_id):
    #     all_ninjas = []
    #     query = """
    #             SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
    #             WHERE dojos.id = %(dojo_id);
    #             """
    #     result = connectToMySQL(DATABASE).query_db(query,{'dojo_id':dojo_id})
    #     for ninja in result:
    #         all_ninjas.append(cls(ninja))
    #     return all_ninjas
    
    @classmethod
    def create_ninja(cls,data_dict):
        query = """
                    INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
                    VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
                """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    

