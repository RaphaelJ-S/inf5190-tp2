from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

import app.src.service.service as serv

app = Flask(__name__, static_folder="static", static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///base_donnees/data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def accueil():

    serv.lireSite()
    return render_template("accueil.html")


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
