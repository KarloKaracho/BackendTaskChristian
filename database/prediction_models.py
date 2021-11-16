from .db import db

class PredictionModel(db.Document):
    name = db.StringField(required=True, unique=True)
    input_var_names = db.ListField(db.StringField(), required=True)
    model_parameter = db.ListField(db.FloatField(), required=True)
    added_by = db.ReferenceField('User')

    def execute(self, input_float_list):
        output = 0
        idx = 0
        for input in input_float_list:
            output = self.model_parameter[idx]* input + output
            idx = idx + 1

        return output

