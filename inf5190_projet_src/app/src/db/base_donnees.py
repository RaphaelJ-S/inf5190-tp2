
from datetime import datetime
from pytz import timezone

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
            adresse=piscine[4],
            propriete=piscine[5],
            gestion=piscine[6],
            point_x=float(piscine[7]),
            point_y=float(piscine[8]),
            equipement=piscine[9],
            longitude=float(piscine[10]),
            latitude=float(piscine[11]),
            arrondissement=piscine[3]
        ))
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

    def get_arrondissement_avec_nom(self, nom: str) -> Arrondissement:
        return Arrondissement.query.filter_by(nom=nom).first()

    def ajouter_source(self, source: list[str]):
        if len(source) > 2:
            self.db.session.add(Source(url=source[0],
                                       parser=source[1],
                                       date_modif=source[2]))
        else:
            self.db.session.add(Source(url=source[0],
                                       parser=source[1]))
        self.db.session.commit()

    def ajouter_sources(self, sources: list[list[str]]):
        for source in sources:
            if len(source) > 2:
                self.db.session.add(Source(url=source[0],
                                           parser=source[1],
                                           date_modif=source[2]))
            else:
                self.db.session.add(Source(url=source[0],
                                           parser=source[1]))
        self.db.session.commit()

    def ajouter_arrondissement(self, arrondissement: str):
        if self.get_arrondissement_avec_nom(arrondissement) is None:
            self.db.session.add(Arrondissement(nom=arrondissement))

    def ajouter_glissades(self, glissades: list[list[str]]):
        with self.app.app_context():
            for glissade in glissades:
                self.ajouter_arrondissement(glissade[5])
                self.db.session.add(Glissade(
                    nom=glissade[2],
                    ouvert=glissade[0],
                    deblaye=glissade[1],
                    cle=glissade[3],
                    date_maj=glissade[4],
                    nom_arr=glissade[5]))
            self.db.session.commit()

    def ajouter_patinoires(self, patinoires: list[list[str]]):
        with self.app.app_context():
            for patinoire in patinoires:
                self.ajouter_arrondissement(patinoire[5])

                self.db.session.add(Patinoire(
                    nom=patinoire[2],
                    date_heure=patinoire[0],
                    deblaye=patinoire[1],
                    arrose=patinoire[3],
                    resurface=patinoire[4],
                    nom_arr=patinoire[5]))
            self.db.session.commit()

    def ajouter_piscines(self, piscines: list[list[str]]):
        with self.app.app_context():
            for piscine in piscines:
                self.ajouter_arrondissement(piscine[3])
                self.db.session.add(Piscine(
                    id_uev=int(piscine[0]),
                    type=piscine[1],
                    nom=piscine[2],
                    adresse=piscine[4],
                    propriete=piscine[5],
                    gestion=piscine[6],
                    point_x=piscine[7].replace(",", "."),
                    point_y=piscine[8].replace(",", "."),
                    equipement=piscine[9],
                    longitude=piscine[10].replace(",", "."),
                    latitude=piscine[11].replace(",", "."),
                    nom_arr=piscine[3]
                ))
            self.db.session.commit()

    def maj_date_sources(self, nom_tables: list[str]):
        est_timezone = timezone("Canada/Eastern")
        with self.app.app_context():
            for nom in nom_tables:
                Source.query.filter_by(
                    parser=nom).update(dict(date_modif=str(
                        datetime.utcnow().astimezone(est_timezone))))

            self.db.session.commit()
