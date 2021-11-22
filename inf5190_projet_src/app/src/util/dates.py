from datetime import datetime
from pytz import UTC, timezone


def now_ET_avec_offset() -> datetime:
    return datetime.utcnow().astimezone(timezone("Canada/Eastern"))


def convertir_str_vers_date_ET_avec_offset(date: str) -> datetime:
    iso = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
    return iso.astimezone(UTC).astimezone(timezone("Canada/Eastern"))
