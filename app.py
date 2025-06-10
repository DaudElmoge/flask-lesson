from flask import Flask

app = Flask(__name__)


@app.route("/",methods=["POST"])
def index():
    return {"message":"Welcome to my first flask app"}

#C.R.U.D

#CREATE -> POST ->/categories
#READ -> GET -> All categories ->/categories
#READ -> GET -> Single category ->/categories/<id> (UPDATE -> PATCH), (DELETE)

#create a single category
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