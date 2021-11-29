from app.src.service.service import Service
from app.src.message.messagerie import Messagerie


class MAJ:
    def __init__(self, service: Service):
        self.service = service

    def trouver_diff_installations(self, nv_donnees: dict):
        nom_tables = list(nv_donnees)
        changements = {}
        for nom in nom_tables:
            anc_donnees = self._get_anciennes_donnees(nom)
            diff = self._diff_installation(
                anc_donnees, nv_donnees[nom])
            changements[nom] = diff
        return changements

    def _get_anciennes_donnees(self, nom: str) -> list[list[str]]:
        representables = self.service.get_donnees(nom)
        for rep in representables:
            rep = rep.as_partial_list()
        return representables

    def _diff_installation(self,
                           anc_donnees: list[list[str]],
                           nv_donnees: list[list[str]]
                           ) -> tuple[list[list[str]]]:
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
        anc_donnees.pop(index_i)
        nv_donnees.pop(index_y)
        return 1

    def effectuer_changements(
            self,
            a_effectuer: dict[str, tuple[list[list[str]]]]) -> list[str]:
        liste_nom_table = list(a_effectuer)
        messagerie = Messagerie()
        for nom in liste_nom_table:
            self.operations_ajout(a_effectuer[nom][0], nom, messagerie)
            # Ces fonctionnalités ne font pas partie du TP mais elle sont
            # gardées pour développement futur
            # self.operations_suppression(a_effectuer[nom][1], nom)
            # self.operations_modification(a_effectuer[nom][2], nom)
        messagerie.executer_envois()
        return liste_nom_table

    def operations_suppression(self, supp: list[list[str]], table: str):
        return  # print("Suppression dans " + table + " : " + str(supp))

    def operations_modification(self, modif: list[list[str]], table: str):
        return  # print("Modification dans " + table + " : " + str(modif))

    def operations_ajout(self,
                         ajout: list[list[str]],
                         table: str,
                         messagerie: Messagerie):
        if ajout:
            self.service.ajouter_donnees(ajout, table)
            messagerie.planifier_envois("Ajout", ajout, table)
