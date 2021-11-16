import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kateisnosto_toimii_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(241)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(241), 1)

    def test_kateisnosto_toimii_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(401)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(401), 1)

    def test_kateisnosto_ei_tarpeeksi_rahaa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)

    def test_kateisnosto_ei_tarpeeksi_rahaa_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)
    
    def test_korttiosto_toimii_edullisesti(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)
        return True
    
    def test_korttiosto_toimii_maukkaasti(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 1)
        return True

    def test_korttiosto_ei_tarpeeksi_rahaa_edullisesti(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
        return False

    def test_korttiosto_ei_tarpeeksi_rahaa_maukkaasti(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
        return False

    def test_ladataan_kortille(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+100)
        self.assertEqual(maksukortti.saldo, 100)

    def test_ladataan_kortille_negatiivinen(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(maksukortti.saldo, 0)