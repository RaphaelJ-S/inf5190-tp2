from app.src.db.init_db import db


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), unique=True, nullable=False)
    parser = db.Column(db.String(50), nullable=False)
    date_modif = db.Column(db.String(30), nullable=True,
                           default="1000-01-01 00:00:00+00:00")
