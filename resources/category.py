from flask_restful import Resource

from models import Category

"""
-> We define our methods using http verbs
   i.e get,post,patch,delete
"""

class CategoryResource(Resource):
    def get(self, id = None):
        if id == None:
            categories = Category.query.all()
            print(categories)
            return categories
        else:
            category = Category.query.filter_by(id = id).first()
            print(category)
            return category
        
    def post (self):
        pass