from .db import db

class ApiCallTracking(db.Document):
    api_name = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    called_by = db.ReferenceField('User')
    model_called = db.ReferenceField('PredictionModel')

