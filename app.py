from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from models import db
from resources.entry import EntryResource
from resources.category import CategoryResource

app = Flask(__name__)

#configure our flask app through the config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notebook.db"

#allow sqlalchemy to display generate sql on the terminal
app.config["SQLALCHEMY_ECHO"] = True

#link flask-restful api
api= Api(app)

#create a migrate object to manage migrations
migrate = Migrate(app, db)

#link our db to the flask app
db.init_app(app)

@app.route("/",methods=["POST"])
def index():
    return {"message":"Welcome to my first flask app"}

#C.R.U.D

#CREATE -> POST ->/categories
#READ -> GET -> All categories ->/categories
#READ -> GET -> Single category ->/categories/<id> (UPDATE -> PATCH), (DELETE)

#create a single category
"""
@app.post("/categories")
def create_category():
    return {"message": "Category created"}

#retrieves all categories
@app.get("/categories")
def get_categories():
    return []

#retrieve a single category
@app.get("/categories/<int:id>")
def get_category(id):
    return {}

#update a single category
@app.patch("/categories/<int:id>")
def update_category(id):
    return {"message": "Category updated"}

#delete a single category
@app.delete("/categories/<int:id>")
def delete_category(id):
    return {"message": "Category deleted"}
"""


api.add_resource(EntryResource, "/entries", "/entries/<entry_id>")
api.add_resource(CategoryResource, "/categories" ,"/categories/<int:id>")