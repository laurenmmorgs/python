from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
mydb ='dojos_and_ninjas'


class Ninjas:
      def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.age = data['age']
            self.dojo_id = data['dojo_id']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            
      @classmethod
      def save(cls,data):
            print(data)
            query='''
            INSERT INTO ninjas 
            (first_name,last_name,age)
            VALUES(%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s);'''
            connectToMySQL(mydb).query_db(query,data)

      @classmethod 
      def get_all_ninjas(cls):
            query = '''
            SELECT * FROM ninjas;'''
            results = connectToMySQL(mydb).query_db(query)
            output = []
            for ninja in results:
                  output.append(cls(ninja))
            return output
      
      @classmethod
      def getByID(cls,data):
            query = '''
            SELECT * 
            FROM ninjas
            WHERE dojo_id = %(dojo_id)s;'''
            results = connectToMySQL(mydb).query_db(query,data)
            return cls(results[0])