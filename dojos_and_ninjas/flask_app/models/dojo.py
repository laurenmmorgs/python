from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
mydb ='dojos_and_ninjas'



class Dojos:
   def __init__(self, data):
      self.created_at = data['created_at'],
      self.updated_at = data['updated_at'],
      self.name = data['name']
      self.id = data['id']
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
      (name)
      VALUES(%(name)s);'''
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
      SELECT ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, dojos.name, dojos.id
      FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
      WHERE dojos.id = %(id)s;'''
      results = connectToMySQL(mydb).query_db(query,data)
      print(results)
      dojo = cls(results[0])
      for ninjas_in_dojos in results:
         ninja_data = {
            'id': ninjas_in_dojos['ninjas.id'],
            'first_name': ninjas_in_dojos['ninjas.first_name'],
            'last_name': ninjas_in_dojos['ninjas.last_name'],
            'age': ninjas_in_dojos['ninjas.age'],
            'dojo_id': ninjas_in_dojos['ninjas.dojo_id'],
            'created_at': ninjas_in_dojos['ninjas.created_at'],
            'updated_at': ninjas_in_dojos['ninjas.updated_at']
         }
         dojo.ninjas.append(ninja.Ninjas(ninja_data))
         print(f' This is for the class method {dojo}')
      return dojo 
