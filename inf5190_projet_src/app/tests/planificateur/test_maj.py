import unittest
from unittest.mock import MagicMock
from app.src.planificateur.maj import MAJ


class Test_MAJ(unittest.TestCase):
    maj = MAJ(MagicMock())

    def test_diff_installations_0changements(self):
        anc_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"]]
        nv_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"]]

        changements = self.maj._diff_installation(anc_donnees, nv_donnees)
        self.assertFalse(changements[0])
        self.assertFalse(changements[1])
        self.assertFalse(changements[2])

    def test_diff_installations_1modif(self):
        anc_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"]]
        nv_donnees = [["deux", "deux", "nom1"], ["deux", "trois", "nom2"]]

        changements = self.maj._diff_installation(anc_donnees, nv_donnees)

        self.assertFalse(changements[0])
        self.assertFalse(changements[1])
        self.assertEqual(changements[2], [["deux", "deux", "nom1"]])

    def test_diff_installations_2modif(self):
        anc_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"]]
        nv_donnees = [["deux", "deux", "nom1"], ["deux", "quatre", "nom2"]]

        changements = self.maj._diff_installation(anc_donnees, nv_donnees)

        self.assertFalse(changements[0])
        self.assertFalse(changements[1])
        self.assertEqual(changements[2], [
            ["deux", "deux", "nom1"], ["deux", "quatre", "nom2"]])

    def test_diff_installations_1ajout(self):
        anc_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        nv_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"], ["deux", "deux", "nom5"]]

        changements = self.maj._diff_installation(anc_donnees, nv_donnees)

        self.assertEqual(changements[0], [["deux", "deux", "nom5"]])
        self.assertFalse(changements[1])
        self.assertFalse(changements[2])

    def test_diff_installations_2ajout(self):
        anc_donnees = [["un", "deux", "nom1"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        nv_donnees = [["deux", "deux", "nom5"], ["un", "deux", "nom1"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]

        changements = self.maj._diff_installation(anc_donnees, nv_donnees)
        self.assertEqual(changements[0], [
            ["deux", "deux", "nom5"], ["sept", "quinze", "nom6"]])
        self.assertFalse(changements[1])
        self.assertFalse(changements[2])

    def test_diff_installations_5ajout(self):
        anc_donnees = []
        nv_donnees = [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        changements = self.maj._diff_installation(anc_donnees, nv_donnees)
        self.assertEqual(changements[0], [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]])
        self.assertFalse(changements[1])
        self.assertFalse(changements[2])

    def test_diff_installations_1supp(self):
        anc_donnees = [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        nv_donnees = [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        changements = self.maj._diff_installation(anc_donnees, nv_donnees)

        self.assertFalse(changements[0])
        self.assertEqual(changements[1], [["deux", "trois", "nom2"]])
        self.assertFalse(changements[2])

    def test_diff_installations_2supp(self):
        anc_donnees = [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        nv_donnees = [["deux", "deux", "nom5"], [
            "un", "quatre", "nom3"], ["deux", "trois", "nom2"]]
        changements = self.maj._diff_installation(anc_donnees, nv_donnees)
        self.assertFalse(changements[0])
        self.assertEqual(changements[1], [
                         ["sept", "quinze", "nom6"], ["cinq", "dix", "nom4"]])
        self.assertFalse(changements[2])

    def test_diff_installations_5supp(self):
        anc_donnees = [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]]
        nv_donnees = []
        changements = self.maj._diff_installation(anc_donnees, nv_donnees)
        self.assertFalse(changements[0])
        self.assertEqual(changements[1], [["deux", "deux", "nom5"], ["sept", "quinze", "nom6"], ["deux", "trois", "nom2"], [
            "un", "quatre", "nom3"], ["cinq", "dix", "nom4"]])
        self.assertFalse(changements[2])

    def test_diff_installations_2supp_3ajout(self):
        anc_donnees = [["deux", "trois", "nom3"], [
            "quatre", "un", "nom1"], ["six", "huit", "nom12"]]
        nv_donnees = [["dix", "deux", "nom4"], ["douze", "quatre", "nom6"], [
            "quatre", "un", "nom1"], ["sept", "onze", "nom10"]]
        changements = self.maj._diff_installation(anc_donnees, nv_donnees)

        self.assertEqual(changements[0], [["dix", "deux", "nom4"], [
                         "douze", "quatre", "nom6"], ["sept", "onze", "nom10"]])
        self.assertEqual(changements[1], [
                         ["deux", "trois", "nom3"], ["six", "huit", "nom12"]])
        self.assertFalse(changements[2])

    def test_diff_installations_listes_vides(self):
        anc_donnees = []
        nv_donnees = []
        changements = self.maj._diff_installation(anc_donnees, nv_donnees)
        self.assertFalse(changements[0])
        self.assertFalse(changements[1])
        self.assertFalse(changements[2])
