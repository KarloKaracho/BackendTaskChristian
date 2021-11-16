from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from database.prediction_models import PredictionModel
import json

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    prediction_models = db.ListField(db.ReferenceField('PredictionModel', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(PredictionModel, 'added_by', db.CASCADE)