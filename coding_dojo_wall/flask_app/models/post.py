from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
mydb = 'users_posts'


class Posts: 
    def __init__(self, data):
      self.id = data['id']
      self.content = data['content']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']
      self.user_id = data['user_id']
      self.creator = None #This is used for a current empty space for a single user dictionary 

    @classmethod
    def save(cls,data):
            print(data)
            query='''
            INSERT INTO posts 
            (content,user_id,created_at, updated_at)
            VALUES(%(content)s,%(user_id)s, NOW(), NOW());'''
            return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_users_with_posts(cls):
        query='''
        SELECT * FROM posts JOIN users ON posts.user_id = users.id;'''
        results = connectToMySQL(mydb).query_db(query)
        all_posts = []
        for posts in results:
            one_post = cls(posts)
            one_post_creator_info = {
                'id': posts['users.id'],
                'email': posts['email'],
                'password': posts['password'],
                'first_name': posts['first_name'],
                'last_name': posts['last_name'],
                'content': posts['content'],
                'created_at': posts['created_at'],
                'updated_at': posts['updated_at']
            }
            author = user.Users(one_post_creator_info)
            one_post.creator = author
            all_posts.append(one_post)
        return all_posts
    
    @classmethod
    def deleteById(cls, data):
            query = '''
            DELETE FROM post  
            WHERE user_id =(%(user_id)s);'''
            results = connectToMySQL(mydb).query_db(query,data)