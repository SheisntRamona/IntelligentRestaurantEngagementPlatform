from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    cuisine_type = db.Column(db.String(80), nullable=False)
    about_us = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

def setup_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/restaurantdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
