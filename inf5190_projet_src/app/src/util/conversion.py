from app.src.model.piscine import Piscine
from app.src.model.patinoire import Patinoire
from app.src.model.glissade import Glissade


def convertir_liste_en_model(donnees: list[list[str]],
                             nom_table: str) -> list:
    if nom_table == "glissade":
        return [str_vers_glissade(x) for x in donnees]
    elif nom_table == "patinoire":
        return [str_vers_patinoire(x) for x in donnees]
    elif nom_table == "piscine":
        return [str_vers_piscine(x) for x in donnees]


def convertir_model_en_liste(donnees: list) -> list[list[str]]:
    return [x.as_partial_list() for x in donnees]


def str_vers_piscine(donnees: list[str]) -> Piscine:
    return Piscine(
        id_uev=int(donnees[0]),
        type=donnees[1],
        nom=donnees[2],
        adresse=donnees[4],
        propriete=donnees[5],
        gestion=donnees[6],
        point_x=donnees[7].replace(",", "."),
        point_y=donnees[8].replace(",", "."),
        equipement=donnees[9],
        longitude=donnees[10].replace(",", "."),
        latitude=donnees[11].replace(",", "."),
        nom_arr=donnees[3]
    )


def str_vers_patinoire(donnees: list[str]) -> Patinoire:
    return Patinoire(
        nom=donnees[2],
        date_heure=donnees[0],
        deblaye=donnees[1],
        arrose=donnees[3],
        resurface=donnees[4],
        nom_arr=donnees[5])


def str_vers_glissade(donnees: list[str]) -> Patinoire:
    return Glissade(
        nom=donnees[2],
        ouvert=donnees[0],
        deblaye=donnees[1],
        cle=donnees[3],
        date_maj=donnees[4],
        nom_arr=donnees[5])
