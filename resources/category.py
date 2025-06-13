from flask import request, jsonify
from flask_restful import Resource


from models import Category, db

"""
-> We define our methods using http verbs
   i.e get,post,patch,delete
"""

class CategoryResource(Resource):
    def get(self, id = None):
        if id == None:
            categories = Category.query.all()
           
            return jsonify([categories.to_dict() for category in categories])
        else:
            category = Category.query.filter_by(id = id).first()
           
            return jsonify(category.to_dict())
        
    def post (self):
        data = request.get_json()
        category = Category (name = data["name"])

        db.session.add(category)
        db.session.commit()

        return {"message":"Category added successfully"}, 201