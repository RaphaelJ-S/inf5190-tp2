from app.src.app import db
from app.src.model.piscine import Piscine


def ajouter_piscine(piscine: list[str]):
    db.session.add(Piscine(
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
    db.session.commit()


db.create_all()
