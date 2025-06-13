from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

#initialize meta data -> ALLOWS US TO DEFINE TABLES AND COLUMNS
metadata = MetaData()

#CREATE A DB INSTANCE
db = SQLAlchemy(metadata = metadata)

""" rules for creating models
-> must have the __tablename__ attribute
-> must have atleast one column
-> we must inherit now from db.model
"""

"""relationship between classes and tables
-> A whole class references a table
-> Instances of the class are rows
-> Attributes are columns
"""

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column (db.Integer, primary_key =True)
    name = db.Column (db.Text, nullable = False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())

    def to_dict(self):
        return {"id":self.id, "name":self.name}
