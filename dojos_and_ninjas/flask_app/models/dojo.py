from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninjas
from pprint import pprint
mydb ='dojos_and_ninjas'



class Dojos:
   def __init__(self, data):
      self.id = data['id']
      self.name = data['name']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']
      self.ninjas = []


   @classmethod
   def get_all(cls):
      query='''
      SELECT * 
      FROM dojos;'''
      results = connectToMySQL(mydb).query_db(query)
      output = []
      for row in results:
         output.append(cls(row))
      return output
   
   @classmethod
   def save(cls,data):
      query='''
      INSERT INTO dojos 
      (name, created_at, updated_at)
      VALUES(%(name)s, NOW(),NOW());'''
      results = connectToMySQL(mydb).query_db(query,data)
      return results 

   @classmethod
   def getByID(cls,data):
      query = '''
         SELECT * 
         FROM dojos
         WHERE id = %(id)s;'''
      results = connectToMySQL(mydb).query_db(query,data)
      return cls(results[0])

   @classmethod
   def get_ninja_with_dojos(cls,data):
      query= '''
      SELECT *
      FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id
      WHERE dojos.id = %(dojo_id)s;'''
      results = connectToMySQL(mydb).query_db(query,data)
      print(results)
      dojo = cls(results[0])
      for ninjas_in_dojos in results:
         ninja_data = {
            'id': ninjas_in_dojos['ninjas.id'],
            'first_name': ninjas_in_dojos['first_name'],
            'last_name': ninjas_in_dojos['last_name'],
            'age': ninjas_in_dojos['age'],
            'dojo_id': ninjas_in_dojos['dojo_id'],
            'created_at': ninjas_in_dojos['ninjas.created_at'],
            'updated_at': ninjas_in_dojos['ninjas.updated_at']
         }
         dojo.ninjas.append(Ninjas(ninja_data))
      return dojo 
