
from flask import Flask
from flask import g
from flask import request
from flask import redirect
from flask.helpers import make_response
from flask.json import jsonify
from flask.templating import render_template
from itsdangerous import BadSignature
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError

from app.src.db.init_db import db
from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.planificateur import Planificateur
from app.src.service.service import Service
from app.src.schema.schema import nv_profil_schema

app = Flask(__name__, static_folder="static", static_url_path="")
schema = JsonSchema(app)

# fichier de configuration yaml pour les courriels et les tweets
FICH_YAML = "app/src/fichier/dest_courriel.yaml"


def creer_app():
    """
    Configure l'application Flask et créé les tables dans la base de données
    si elles ne sont pas déjà créées.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()


def get_db():
    """
    Retourne une instance singleton de la classe qui s'occupe de communiquer
    avec la base de données.
    """
    database = getattr(g, '_database', None)
    if database is None:
        g._database = Base_Donnees(db, app)
    return g._database


@app.before_first_request
def initialiser_planificateur():
    """
    Initialise le planificateur qui s'occupe des opérations planifiées.
    """
    # décommentez pour faire un téléchargement immédiatement
    #  après la première requête
    # planificateur = Planificateur(get_db(), 5)
    # décommentez pour changer l'heure de téléchargement à 1 fois / 24h
    planificateur = Planificateur(get_db())
    planificateur.run()


# Routes

@app.route("/")
def accueil():
    """
    Page d'accueil de l'application.
    """
    serv = Service(get_db())
    nom_installations = serv.get_nom_installations()
    return render_template("form_installations.html",
                           installations=nom_installations)


@app.route("/doc")
def documentation():
    """
    Page de documentation des API de l'application.
    """
    return render_template("documentation.html")


@app.route("/profil", methods=["GET"])
def formulaire_profil():
    """
    Page de création d'un profil.
    """
    return render_template("form_profil.html")


@app.route("/desabonnement/<token>")
def desabonnement(token):
    """
    Page de confirmation d'un desabonnement.
    """
    return render_template("desabonnement.html")


# API


@app.route("/api/arrondissements")
def tous_arrondissements():
    """
    Retourne le nom de tous les arrondissements.
    """
    service = Service(get_db())
    arrondissements = service.get_noms_arrondissements()
    return jsonify(arrondissements)


@app.route("/api/installations")
def selection_installations():
    """
    Retourne les installations de l'arrondissement donné en query string.
    """
    service = Service(get_db())
    try:
        installations = service.get_installations(
            request.args.get("arrondissement"))
    except ValueError as ve:
        return make_response(jsonify(ve.args), 404)
    except TypeError as te:
        return make_response(jsonify(te.args), 400)
    return jsonify(installations)


@app.route("/api/installation")
def selection_installation():
    """
    Retourne les informations de l'installation donnée en query string.
    """
    service = Service(get_db())
    try:
        installation = service.get_installation(
            request.args.get("installation"))
        return jsonify(installation)
    except ValueError as ve:
        return make_response(jsonify(ve.args), 404)
    except TypeError as te:
        return make_response(jsonify(te.args), 400)


@app.route("/api/profil", methods=["POST"])
@schema.validate(nv_profil_schema)
def creer_profil():
    """
    Crée un nouveau profil d'utilisateur cherchant à reçevoir des
    courriels quant aux installations.
    Reçoit un corps JSON validé par un schema json.
    """
    nouveau_profil = request.get_json()
    service = Service(get_db())
    try:
        service.creer_nouveau_profil(FICH_YAML, nouveau_profil)
    except ValueError as ve:
        return make_response(jsonify(ve.args), 400)
    return make_response(jsonify("Le nouveau profil a été créé avec succès"),
                         201)


@app.route("/api/desabonnement/<token>", methods=["DELETE"])
def supprimer_profil(token):
    """
    Supprime tous les profils correspondants à @token.
    @token : L'identifiant d'un profil.
    """
    service = Service(get_db())
    try:
        service.supprimer_profil(FICH_YAML, token)
    except OSError as ose:
        return jsonify(ose.args), 500
    except BadSignature or ValueError as err:
        return jsonify(err.args), 400

    return make_response(jsonify("Profil supprimé avec succès"), 200)


@app.errorhandler(JsonValidationError)
def validation(erreur):
    erreurs = [err.message for err in erreur.errors]
    return jsonify({"erreur": erreur.message, "erreurs": erreurs})


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def erreur_handler(erreur):
    if request.path.startswith("/api/"):
        return jsonify(str(erreur)), erreur.code
    else:
        print(erreur.code)
        return render_template("erreur.html", erreur=erreur.code)


def main():
    creer_app()
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
