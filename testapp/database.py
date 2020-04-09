from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    global db
    db.init_app(app)
