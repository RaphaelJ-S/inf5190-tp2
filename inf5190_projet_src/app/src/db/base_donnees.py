

from app.src.util.dates import now_ET_avec_offset
from app.src.model.piscine import Piscine
from app.src.model.source import Source
from app.src.model.glissade import Glissade
from app.src.model.patinoire import Patinoire
from app.src.model.arrondissement import Arrondissement
import app.src.util.conversion as conv


class Base_Donnees():
    def __init__(self, type_db, app):
        self.db = type_db
        self.app = app

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

    def get_piscine_avec_nom(self, nom_installation: str) -> Piscine:
        with self.app.app_context():
            return Piscine.query.filter_by(nom=nom_installation).first()

    def get_patinoire_avec_nom(self, nom_installation: str) -> Patinoire:
        with self.app.app_context():
            return Patinoire.query.filter_by(nom=nom_installation).first()

    def get_glissade_avec_nom(self, nom_installation: str) -> Glissade:
        with self.app.app_context():
            return Glissade.query.filter_by(nom=nom_installation).first()

    def get_arrondissements(self) -> list[Arrondissement]:
        with self.app.app_context():
            return Arrondissement.query.all()

    def get_arrondissement_avec_nom(self, nom: str) -> Arrondissement:
        return Arrondissement.query.filter_by(nom=nom).first()

    def get_installations(self) -> list:
        with self.app.app_context():
            piscines_q = self.get_piscines()
            patinoires_q = self.get_patinoires()
            glissades_q = self.get_glissades()
            return piscines_q, patinoires_q, glissades_q

    def get_installations_avec_arrondissement(self, nom_arr: str) -> list:
        with self.app.app_context():
            piscines_q = (self.db.session.query(
                Arrondissement, Piscine)
                .filter_by(nom=nom_arr)
                .join("piscines")
            ).all()
            patinoires_q = (self.db.session.query(
                Arrondissement, Patinoire)
                .filter_by(nom=nom_arr)
                .join("patinoires")
            ).all()
            glissades_q = (self.db.session.query(
                Arrondissement, Glissade)
                .filter_by(nom=nom_arr)
                .join("glissades")
            ).all()
            return piscines_q, patinoires_q, glissades_q

    def ajouter_source(self, source: list[str]):
        with self.app.app_context():

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
                self.db.session.add(conv.str_vers_glissade(glissade))
            self.db.session.commit()

    def ajouter_patinoires(self, patinoires: list[list[str]]):
        with self.app.app_context():
            for patinoire in patinoires:
                self.ajouter_arrondissement(patinoire[5])
                self.db.session.add(conv.str_vers_patinoire(patinoire))
            self.db.session.commit()

    def ajouter_piscines(self, piscines: list[list[str]]):
        with self.app.app_context():
            for piscine in piscines:
                self.ajouter_arrondissement(piscine[3])
                self.db.session.add(conv.str_vers_piscine(piscine))
            self.db.session.commit()

    def maj_date_sources(self, nom_tables: list[str]):
        with self.app.app_context():
            for nom in nom_tables:
                Source.query.filter_by(
                    parser=nom).update(dict(date_modif=str(
                        now_ET_avec_offset())))

            self.db.session.commit()
