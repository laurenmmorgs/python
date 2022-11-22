#this represents our USERS table in our database
from flask_app.config.mysqlconnection import connectToMySQL 
from pprint import pprint
mydb = 'users' #! tells us what schema we want to access

class Users: 
   def __init__(self, data): #!var that carries data in this case it is stuff
      self.id =data['id'] #! keys from the column names in our database
      self.first_name = data['first_name']
      self.last_name = data['last_name']
      self.email = data['email']
      self.created_at = data['created_at']

   @classmethod #! this has to be in the class so no indentation
   def get_all(cls): #!dont forget the cls part so we can access it 
      query = '''
      SELECT * 
      FROM users;'''
      results = connectToMySQL(mydb).query_db(query)
      pprint(results) 
      output =[]
      for row in results:
         output.append(cls(row))  #!This puts the users inside the SQL DATABASE 
         # print(output)
      return output
   
   @classmethod
   def save(cls,data):
      query = '''
      INSERT INTO users
      (first_name, last_name, email)
      VALUES(%(first_name)s, %(last_name)s, %(email)s);'''
      results = connectToMySQL(mydb).query_db(query,data)
      # print(f"results: {results}")
      return results

   @classmethod
   def deleteById(cls, data):
      query = '''
      DELETE FROM users 
      WHERE id =(%(id)s);'''
      results = connectToMySQL(mydb).query_db(query,data)
      