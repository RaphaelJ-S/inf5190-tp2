from datetime import datetime
from pytz import UTC, timezone


def now_ET_avec_offset() -> datetime:
    """
    Retourne la date et l'heure à l'instant même du fuseau horaire
    Canada - Est en format ISO avec offset.
    @return la date/heure de 'now'.
    """
    return datetime.utcnow().astimezone(timezone("Canada/Eastern"))


def convertir_str_vers_date_ET_avec_offset(date: str) -> datetime:
    """
    Transforme une chaîne de format 'JourDeLaSemaine, DateDuMois
    NomDuMois Annee Heure:Minute:Seconde Timezone' en format ISO
    avec offset du fuseau horaire Can/Est.
    """
    iso = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
    return iso.astimezone(UTC).astimezone(timezone("Canada/Eastern"))
