
from flask import Flask, g
from flask.templating import render_template

from app.src.db.init_db import db
from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.planificateur import Planificateur
import app.src.service.service as serv

app = Flask(__name__, static_folder="static", static_url_path="")


def creer_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()


def get_db():
    database = getattr(g, '_database', None)
    if database is None:
        g._database = Base_Donnees(db, app)
    return g._database


@app.before_first_request
def initialiser_planificateur():
    planificateur = Planificateur(get_db(), 5)
    planificateur.run()


@app.route("/")
def accueil():
    return render_template("accueil.html")


@app.route("/doc")
def documentation():
    return render_template("documentation.html")


def main():
    creer_app()
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
