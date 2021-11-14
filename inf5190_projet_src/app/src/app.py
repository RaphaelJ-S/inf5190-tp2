
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template


app = Flask(__name__, static_folder="static", static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# doit être importé pour ne pas causer d'importation circulaire
import app.src.db.data as database
from app.src.planificateur.planificateur import Planificateur
import app.src.service.service as serv


@app.before_first_request
def initialiser_planificateur():
    planificateur = Planificateur(20)
    planificateur.run()


@app.route("/")
def accueil():
    return render_template("accueil.html")


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
