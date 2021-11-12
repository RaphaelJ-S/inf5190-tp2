
import app.src.db.data as database


def ajouter_piscine():
    toutes_piscines = list(cr)
    toutes_piscines[1][7] = toutes_piscines[1][7].replace(",", ".")
    print(toutes_piscines[1][7])
    database.ajouter_piscine(toutes_piscines[1])
