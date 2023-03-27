import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), f"Kortilla on rahaa {round(1000 / 100, 2)}0 euroa")

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_lataaminen_kasvattaa_korttiarvoa_oikein(self):
        lataus_maara = 500
        self.maksukortti.lataa_rahaa(lataus_maara)
        self.assertEqual(str(self.maksukortti), f"Kortilla on rahaa {round((1000 + lataus_maara)/100, 2)}0 euroa")
    
    def test_rahan_ottaminen_vahentaa_oikein(self):
        vahennys_maara = 500
        self.maksukortti.ota_rahaa(vahennys_maara)
        self.assertEqual(str(self.maksukortti), f"Kortilla on rahaa {round((1000 - vahennys_maara)/100, 2)}0 euroa")
    
    def test_rahan_ottaminen_ei_vie_negatiiviseksi(self):
        vahennys_maara = 1500
        self.maksukortti.ota_rahaa(vahennys_maara)
        self.assertEqual(str(self.maksukortti), f"Kortilla on rahaa 10.00 euroa")
    
    def test_palauttaa_true_kun_raha_riittaa(self):
        vahennys_maara = 500
        self.maksukortti.ota_rahaa(vahennys_maara)
        self.assertTrue(self.maksukortti.ota_rahaa(vahennys_maara))
    
    def test_palauttaa_false_kun_raha_ei_riita(self):
        vahennys_maara = 1500
        self.maksukortti.ota_rahaa(vahennys_maara)
        self.assertFalse(self.maksukortti.ota_rahaa(vahennys_maara))
    
    
    