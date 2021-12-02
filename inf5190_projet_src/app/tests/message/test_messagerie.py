import unittest
from unittest.mock import MagicMock
from app.src.message.messagerie import Messagerie


class Test_Messagerie(unittest.TestCase):

    def test_charger_adresse_courriel_format_yaml(self):
        msg = Messagerie()

        contenu = msg.charger_contenu_configuration(
            "app/src/fichier/dest_courriel.yaml")
        courriel = contenu["courriel_envoyant"]
        twitter = contenu["compte_twitter"]
        liste_dest = contenu["courriel_cible"]

        assert(contenu and courriel and twitter and liste_dest)
