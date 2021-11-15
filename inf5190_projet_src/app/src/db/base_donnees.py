
from datetime import datetime

import jinja2
from app.src.model.piscine import Piscine
from app.src.model.source import Source
from app.src.model.glissade import Glissade
from app.src.model.patinoire import Patinoire
from app.src.model.arrondissement import Arrondissement


class Base_Donnees():
    def __init__(self, type_db, app):
        self.db = type_db
        self.app = app

    def ajouter_piscine(self, piscine: list[str]):

        self.db.session.add(Piscine(
            id_uev=int(piscine[0]),
            type=piscine[1],
            nom=piscine[2],
            arrondissement=piscine[3],
            adresse=piscine[4],
            propriete=piscine[5],
            gestion=piscine[6],
            point_x=float(piscine[7]),
            point_y=float(piscine[8]),
            equipement=piscine[9],
            longitude=float(piscine[10]),
            latitude=float(piscine[11])))
        self.db.session.commit()

    def ajouter_source(self, source: list[str]):
        if len(source) > 2:
            self.db.session.add(Source(url=source[0],
                                       parser=source[1],
                                       date_modif=source[2]))
        else:
            self.db.session.add(Source(url=source[0],
                                       parser=source[1]))
        self.db.session.commit()

    def get_sources(self) -> list[Source]:
        with self.app.app_context():
            return Source.query.all()

    def get_patinoires(self) -> list[Patinoire]:
        with self.app.app_context():
            return Patinoire.query.all()

    def get_glissades(self) -> list[Glissade]:
        with self.app.app_context():
            return Glissade.query.all()

    def get_piscines(self) -> list[Piscine]:
        with self.app.app_context():
            return Piscine.query.all()

    def get_arrondissements(self) -> list[Arrondissement]:
        with self.app.app_context():
            return Arrondissement.query.all()

    def maj_date_sources(self, nom_tables: list[str]):
        for nom in nom_tables:
            tous_sources_avec_nom = Source.query.filter_by(parser=nom).update(
                dict(date_modif=str(
                    datetime.utcnow().astimezone("Canada/Eastern"))))
            self.db.session.commit()
