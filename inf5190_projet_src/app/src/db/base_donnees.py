

from app.src.util.dates import now_ET_avec_offset
from app.src.model.piscine import Piscine
from app.src.model.source import Source
from app.src.model.glissade import Glissade
from app.src.model.patinoire import Patinoire
from app.src.model.arrondissement import Arrondissement
import app.src.util.conversion as conv


class Base_Donnees:
    """
    Communique et effectue des opération sur la base de données.
    """

    def __init__(self, type_db, app):
        self.db = type_db
        self.app = app

    def get_sources(self) -> list[Source]:
        """
        Retourne toutes les entrées de la table 'source'.
        """
        with self.app.app_context():
            return Source.query.all()

    def get_patinoires(self) -> list[Patinoire]:
        """
        Retourne toutes les entrées de la table 'patinoire'.
        """
        with self.app.app_context():
            return Patinoire.query.all()

    def get_glissades(self) -> list[Glissade]:
        """
        Retourne toutes les entrées de la table 'glissade'.
        """
        with self.app.app_context():
            return Glissade.query.all()

    def get_piscines(self) -> list[Piscine]:
        """
        Retourne toutes les entrées de la table 'piscine'.
        """
        with self.app.app_context():
            return Piscine.query.all()

    def get_arrondissements(self) -> list[Arrondissement]:
        """
        Retourne toutes le entrées de la table 'arrondissement'.
        """
        with self.app.app_context():
            return Arrondissement.query.all()

    def get_piscine_avec_nom(self, nom_installation: str) -> Piscine:
        """
        Retourne la piscine avec le nom @nom_installation.
        """
        with self.app.app_context():
            return Piscine.query.filter_by(nom=nom_installation).all()

    def get_patinoire_avec_nom(self, nom_installation: str) -> Patinoire:
        """
        Retourne la patinoire avec le nom @nom_installation.
        """
        with self.app.app_context():
            return Patinoire.query.filter_by(nom=nom_installation).all()

    def get_glissade_avec_nom(self, nom_installation: str) -> Glissade:
        """
        Retourne la glissade avec le nom @nom_installation.
        """
        with self.app.app_context():
            return Glissade.query.filter_by(nom=nom_installation).all()

    def get_arrondissement_avec_nom(self, nom: str) -> Arrondissement:
        """
        Retourne l'arrondissement avec le nom @nom.
        """
        return Arrondissement.query.filter_by(nom=nom).first()

    def get_installations(self) -> list:
        """
        Retourne toutes les installations des tables 'glissade', 'piscine' et
        'patinoire'.
        @return : Les 3 listes contenant les installations de chaque table.
        l'ordre est : piscine -> patinoire -> glissade
        """
        with self.app.app_context():
            piscines_q = self.get_piscines()
            patinoires_q = self.get_patinoires()
            glissades_q = self.get_glissades()
            return piscines_q, patinoires_q, glissades_q

    def get_installations_avec_arrondissement(self, nom_arr: str) -> list:
        """
        Retourne toutes les installations des tables 'glissade, 'piscine' et
        'patinoire' qui font partie de l'arrondissement @nom_arr.
        @nom_arr : Le nom de l'arrondissement pour lequel on recherche
        les installations.
        @return : Les 3 listes contenant les installations de chaque table.
        l'ordre est : piscine -> patinoire -> glissade.
        """
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
        """
        Ajoute une entrée à la table 'source'.
        @source : Une liste de paramètres.
        """
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
        """
        Ajoute des entrées à la table 'source'.
        @sources : Une liste de liste de paramètres.
        """
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
        """
        Ajoute une entrée à la table 'arrondissement' si cette entrée n'existe
        pas.
        Cette fonction est supposée être utilisée à l'intérieur d'un autre
        appel puisqu'elle ajout simplement l'arrondissement à la session.
        """
        if self.get_arrondissement_avec_nom(arrondissement) is None:
            self.db.session.add(Arrondissement(nom=arrondissement))

    def ajouter_glissades(self, glissades: list[list[str]]):
        """
        Ajoute des entrées à la table 'glissade'.
        """
        with self.app.app_context():
            for glissade in glissades:
                self.ajouter_arrondissement(glissade[5])
                self.db.session.add(conv.str_vers_glissade(glissade))
            self.db.session.commit()

    def ajouter_patinoires(self, patinoires: list[list[str]]):
        """
        Ajoute des entrées à la table 'patinoire'.
        """
        with self.app.app_context():
            for patinoire in patinoires:
                self.ajouter_arrondissement(patinoire[5])
                self.db.session.add(conv.str_vers_patinoire(patinoire))
            self.db.session.commit()

    def ajouter_piscines(self, piscines: list[list[str]]):
        """
        Ajoute des entrées à la table 'piscine'.
        """
        with self.app.app_context():
            for piscine in piscines:
                self.ajouter_arrondissement(piscine[3])
                self.db.session.add(conv.str_vers_piscine(piscine))
            self.db.session.commit()

    def maj_date_sources(self, nom_tables: list[str]):
        """
        Mets à jour les dates de modification de la table 'source' indiquées.
        @nom_tables : les entrées à modifier.
        """
        with self.app.app_context():
            for nom in nom_tables:
                Source.query.filter_by(
                    parser=nom).update(dict(date_modif=str(
                        now_ET_avec_offset())))

            self.db.session.commit()
