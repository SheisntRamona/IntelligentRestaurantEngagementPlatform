from config import db
from sqlalchemy.dialects.postgresql import ARRAY
import json

class FactList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(80), unique=True, nullable=False)
    facts = db.Column(ARRAY(db.String(256)), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "restaurant_name": self.restaurant_name,
            "facts": self.facts
        }

def questionsToJson(questions):
    # Converts questions json string to key value object
    questions_dict = json.loads(questions)
    return questions_dict