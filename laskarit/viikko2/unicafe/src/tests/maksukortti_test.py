import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(100)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortinsaldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_kortille_lataaminen_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 1.5")

    def test_kortin_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_kortin_saldo_ei_muutu_kun_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(110)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    
    def test_kortin_saldo_riittävä(self):
        if self.test_kortin_saldo_vahenee_oikein_kun_rahaa_tarpeeksi:
            return True
        return False