import unittest
from unittest.mock import MagicMock
from app.src.message.messagerie import Messagerie
from itsdangerous import URLSafeTimedSerializer


class Test_Messagerie(unittest.TestCase):

    def test_charger_adresse_courriel_format_yaml(self):
        msg = Messagerie()

        courriel, twitter, liste_dest = msg.charger_contenu_configuration(
            "app/src/fichier/dest_courriel.yaml")

        assert(courriel and twitter and liste_dest)
