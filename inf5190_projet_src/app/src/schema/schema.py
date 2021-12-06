nv_profil_schema = {
    "description": "Création d'un profil pour l'envois de courriels",
    'type': 'object',
    "required": ["nom", "email", "liste_arr"],
    "properties": {
        "nom": {
            "description": "Nom de l'utilisateur",
            "type": "string",
            "minLength": 2,
        },
        "email": {
            "description": "Courriel de l'utilisateur",
            "type": "string",
            "format": "email",
            "pattern": "^[a-zA-Z0-9]+@[A-Za-z0-9]+\.[a-zA-Z]+$",
        },
        "liste_arr": {
            "type": "array",
            "desription": "Arrondissements que l'utilisateur veut suivre",
            "items": {
                "type": "string",
                "minLength": 4,
            },
        },
    }
}
