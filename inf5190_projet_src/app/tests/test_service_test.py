import app.src.service.service as serv
import unittest


class Test(unittest.TestCase):

    def test_prem(self):
        self.assertEqual(10, serv.prem_fonc())

    def test_deux_1(self):
        self.assertEqual(200, serv.deux_fonc(1))

    def test_deux_2(self):
        self.assertEqual(400, serv.deux_fonc(2))

    def test_trois_1(self):
        self.assertEqual(50, serv.trois_fonc(5, 10))

    def test_trois_2(self):
        self.assertEqual(150, serv.trois_fonc(25, 6))

    if __name__ == "__main__":
        unittest.main()
