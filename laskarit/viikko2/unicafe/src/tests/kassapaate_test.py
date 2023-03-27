import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

#Edulliset käteistestit

    def test_kassan_raha_on_oikein(self):
        assert self.kassapaate.kassassa_rahaa / 100 == 1000
        
    def test_kateis_osto_toimii_edullinen(self):
        maksu = 500
        kassa_ennen_maksua = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(maksu)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_maksua + 240
    
    def test_vaihtoraha_oikein_edullinen(self):
        maksu = 500
        assert self.kassapaate.syo_edullisesti_kateisella(maksu) == -(240 - maksu)
    
    def test_myydyt_lounaat_kasvaa_kateinen_edullinen(self):
        edulliset_ennen_ostoa = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kateisella(500)
        assert self.kassapaate.edulliset == edulliset_ennen_ostoa + 1

    def test_riittamaton_maksu_ei_mene_kassaan_edullinen(self):
        maksu = 200
        kassa_ennen_maksua = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(maksu)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_maksua

    
    
    def test_riittamaton_maksu_rahan_palautus_edullinen(self):
        maksu = 200
        assert self.kassapaate.syo_edullisesti_kateisella(maksu) == maksu
    
    def test_riittamaton_maksu_ei_kasvata_lounaita_edullinen(self):
        maksu = 200
        edulliset_ennen_ostoa =self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kateisella(200)
        assert self.kassapaate.edulliset == edulliset_ennen_ostoa



#Maukkaat käteistestit


    def test_kateis_osto_toimii_maukas(self):
        maksu = 500
        kassa_ennen_maksua = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(maksu)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_maksua + 400
    
    def test_vaihtoraha_oikein_maukas(self):
        maksu = 500
        assert self.kassapaate.syo_maukkaasti_kateisella(maksu) == -(400 - maksu)
    
    def test_myydyt_lounaat_kasvaa_kateinen_maukas(self):
        maukkaat_ennen_ostoa = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kateisella(500)
        assert self.kassapaate.maukkaat == maukkaat_ennen_ostoa + 1

    def test_riittamaton_maksu_ei_mene_kassaan_maukas(self):
        maksu = 200
        kassa_ennen_maksua = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(maksu)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_maksua

    
    
    def test_riittamaton_maksu_rahan_palautus_maukas(self):
        maksu = 200
        assert self.kassapaate.syo_maukkaasti_kateisella(maksu) == maksu
    
    def test_riittamaton_maksu_ei_kasvata_lounaita_maukas(self):
        maksu = 200
        maukkaat_ennen_ostoa =self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kateisella(200)
        assert self.kassapaate.maukkaat == maukkaat_ennen_ostoa
    
    
#Edulliset korttiostot

    def test_korttiosto_toimii_edullinen(self):
        korttisaldo_ennen_ostoa = self.maksukortti.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        assert self.maksukortti.saldo == korttisaldo_ennen_ostoa - 240
    
    def test_jos_riittaa_palauttaa_true_edullinen(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_myydyt_lounaat_kasvaa_kortti_edullinen(self):
        edulliset_ennen_ostoa = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        assert self.kassapaate.edulliset == edulliset_ennen_ostoa + 1
    
    def test_raha_ei_muutu_jos_saldo_ei_riita_edullinen(self):
        self.maksukortti = Maksukortti(100)
        korttisaldo_ennen_ostoa = self.maksukortti.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        assert self.maksukortti.saldo == korttisaldo_ennen_ostoa
        

    def test_lounaat_ei_kasva_jos_saldo_ei_riita_edullinen(self):
        self.maksukortti = Maksukortti(100)
        edulliset_ennen_ostoa = self.kassapaate.edulliset
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        assert self.kassapaate.edulliset == edulliset_ennen_ostoa

    def test_jos_ei_riita_palauttaa_false_edullinen(self):
        self.maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        
    def test_kassa_raha_ei_muutu_korttiostoissa_edullinen(self):
        self.maksukortti = Maksukortti(100)
        kassa_ennen_ostoa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_ostoa

#Maukkaat korttiostot

    def test_korttiosto_toimii_maukas(self):
        korttisaldo_ennen_ostoa = self.maksukortti.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        assert self.maksukortti.saldo == korttisaldo_ennen_ostoa - 400
    
    def test_jos_riittaa_palauttaa_true_maukas(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    
    def test_myydyt_lounaat_kasvaa_kortti_maukas(self):
        maukkaat_ennen_ostoa = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        assert self.kassapaate.maukkaat == maukkaat_ennen_ostoa + 1
    
    def test_raha_ei_muutu_jos_saldo_ei_riita_maukas(self):
        self.maksukortti = Maksukortti(100)
        korttisaldo_ennen_ostoa = self.maksukortti.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        assert self.maksukortti.saldo == korttisaldo_ennen_ostoa
        

    def test_lounaat_ei_kasva_jos_saldo_ei_riita_maukas(self):
        self.maksukortti = Maksukortti(100)
        maukkaat_ennen_ostoa = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        assert self.kassapaate.maukkaat == maukkaat_ennen_ostoa

    def test_jos_ei_riita_palauttaa_false_maukas(self):
        self.maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        
    def test_kassa_raha_ei_muutu_korttiostoissa_maukas(self):
        self.maksukortti = Maksukortti(100)
        kassa_ennen_ostoa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_ostoa

    def test_kortin_saldo_muuttuu_ladattaessa(self):
        saldo_ennen_latausta = self.maksukortti.saldo
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        assert self.maksukortti.saldo == saldo_ennen_latausta + 500
    
    def test_kassaan_tulee_rahaa_ladattaessa(self):
        kassa_ennen_latausta = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_latausta + 500
    
    def test_saldo_tai_kassaraha_ei_kasva_jos_latausraha_ei_positiivinen(self):
        kassa_ennen_latausta = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5)
        assert self.kassapaate.kassassa_rahaa == kassa_ennen_latausta
