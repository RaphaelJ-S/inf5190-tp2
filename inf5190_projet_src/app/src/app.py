
from flask import Flask
from flask import g
from flask import request
from flask import redirect
from flask.helpers import make_response
from flask.json import jsonify
from flask.templating import render_template

from app.src.db.init_db import db
from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.planificateur import Planificateur
from app.src.service.service import Service

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
    # décommentez pour faire un téléchargement immédiatement après la première requête
    planificateur = Planificateur(get_db(), 5)
    # décommentez pour changer l'heure de téléchargement à 1 fois / 24h
    # planificateur = Planificateur(get_db())
    planificateur.run()


# Routes

@app.route("/")
def accueil():
    serv = Service(get_db())
    nom_arrs = serv.get_noms_arrondissements()
    return render_template("form_installations.html", arrondissements=nom_arrs)


@app.route("/doc")
def documentation():
    return render_template("documentation.html")


# API

@app.route("/api/installations")
def selection_installations():
    service = Service(get_db())
    try:
        installations = service.get_installations(
            request.args.get("arrondissement"))
    except ValueError as ve:
        return make_response(jsonify(ve.args), 404)
    except TypeError as te:
        return make_response(jsonify(te.args), 400)
    return jsonify(installations)


def main():
    creer_app()
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
