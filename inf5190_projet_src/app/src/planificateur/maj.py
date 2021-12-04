from app.src.service.service import Service
from app.src.message.messagerie import Messagerie
from app.src.util.conversion import convertir_liste_en_model
from app.src.util.conversion import convertir_model_en_liste


class MAJ:
    """
    S'occupe de la mise à jours des données et de toutes opérations reliées
    à ces mises à jours.
    """

    def __init__(self, service: Service):
        self.service = service

    def trouver_diff_installations(self, nv_donnees: dict):
        """
        Trouve les différences entre les données téléchargées et celles dans
        la base de données et les retournent.
        @nv_donnes : Les nouvelles données.
        @return : Les changement apportés aux nouvelles données
        """
        nom_tables = list(nv_donnees)
        changements = {}
        for nom in nom_tables:
            anc_donnees = self._get_anciennes_donnees(nom)
            diff = self._diff_installation(
                anc_donnees, nv_donnees[nom])
            changements[nom] = diff
        return changements

    def _get_anciennes_donnees(self, nom: str) -> list[list[str]]:
        """
        Retourne les données des installations dans la base de données sous
        forme de liste de paramètres.
        @nom : Le nom de la table.
        @return : Les installation de la table @nom sous forme de liste
        de paramètres.
        """
        representables = self.service.get_donnees(nom)
        return convertir_model_en_liste(representables)

    def _diff_installation(self,
                           anc_donnees: list[list[str]],
                           nv_donnees: list[list[str]]
                           ) -> tuple[list[list[str]]]:
        """
        Retourne les différences entre les données sous forme de tuple
        (a_ajouter, a_supprimer, a_modifier).
        @anc_donnes : Des données contenues dans la base de données.
        @nv_donnes : Des données téléchargées.
        @return : Les changements à effectuer.
        """
        modif = []
        range_i = len(anc_donnees)
        i = 0
        delta = 0
        while i < range_i:
            curr_donnees = anc_donnees[i]
            for y in range(len(nv_donnees)):
                if curr_donnees[2] == nv_donnees[y][2]:  # le nom est le même
                    # S'il y a des différences dans les données
                    if curr_donnees != nv_donnees[y]:
                        modif.append(nv_donnees[y])
                    delta = self._enlever_elements(
                        i, y, anc_donnees, nv_donnees)
                    break
            # on modifie les listes alors on doit modifier les index
            i -= delta - 1
            range_i -= delta
            delta = 0
        return (nv_donnees, anc_donnees, modif)

    def _enlever_elements(self, index_i, index_y,
                          anc_donnees: list[list[str]],
                          nv_donnees: list[list[str]]
                          ) -> int:
        """
        Supprime les éléments @index_i, @index_y des données et retourne
        1 pour modifier les delta puisque les listes ont été modifiées.
        @index_i : L'index de la liste anc_donnes.
        @index_y :  L'index de la liste nv_donnes.
        @anc_donnees : Les données de la base de données.
        @nv_donnees : Les nouvelles données.
        @return : 1...
        """
        anc_donnees.pop(index_i)
        nv_donnees.pop(index_y)
        return 1

    def effectuer_changements(
            self,
            a_effectuer: dict[str, tuple[list[list[str]]]]) -> list[str]:
        """
        Effectue les opérations liées aux différents changements à apporter.
        @a_effectuer : les changement à effectuer, organiser par table.
        @return : La liste des nom des tables.
        """
        liste_nom_table = list(a_effectuer)
        messagerie = Messagerie()
        models_ajout = []
        for nom in liste_nom_table:
            a_ajouter = a_effectuer[nom][0]
            if a_ajouter:
                self.service.ajouter_donnees(a_ajouter, nom)
                models_ajout += convertir_liste_en_model(a_ajouter, nom)

            # Ces fonctionnalités ne font pas partie du TP mais elle sont
            # gardées pour développement futur
            # self.operations_suppression(a_effectuer[nom][1], nom)
            # self.operations_modification(a_effectuer[nom][2], nom)
        messagerie.planifier_envois("Ajout", models_ajout)
        messagerie.executer_envois()
        return liste_nom_table

    def operations_suppression(self, supp: list[list[str]], table: str):
        return  # print("Suppression dans " + table + " : " + str(supp))

    def operations_modification(self, modif: list[list[str]], table: str):
        return  # print("Modification dans " + table + " : " + str(modif))
