from app.src.model.piscine import Piscine
from app.src.model.patinoire import Patinoire
from app.src.model.glissade import Glissade


def convertir_liste_en_model(donnees: list[list[str]],
                             nom_table: str) -> list:
    donnees_converties = []
    if nom_table == "glissade":
        for donnee in donnees:
            donnees_converties.append(str_vers_glissade(donnee))
    elif nom_table == "patinoire":
        for donnee in donnees:
            donnees_converties.append(str_vers_patinoire(donnee))
    elif nom_table == "piscine":
        for donnee in donnees:
            donnees_converties.append(str_vers_piscine(donnee))
    return donnees_converties


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
