__author__ = 'rtaylor'

import datetime
import uuid

from src.common.database import Database


#create a class called Post that is an object (object oriented programming)
class Post(object):
#we will define it as an initialization with four parameters: self, title, content, author.
#add a blog_id and id to differentiate the blogs from each other.
    #id has a default parameter, this is only true of end parameters. So if you want to def
    #an initialization that has a parameter with a default, it must be last in the command.
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        # generates a unique identifier if one does not exist
        self._id = uuid.uuid4().hex if id is None else id

#create a way for the object to be saved to a database
    def save_to_mongo(self):
        Database.insert(collection = 'posts' ,
                        data = self.json())

#create a json method to return a json representation of the object
    def json(self):
        return {
            'id' : self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title' : self.title,
            'created_date': self.created_date

        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id:id]'})
        #the ** allows the objects elements to be equal to that in the database
        return cls(**post_data)

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts' , query={'_id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts' , query={'blog_id': id})]
