import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    #Testataan että varaston saldo on alussa 0
    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Onhan varaston tilavuus oikea alussa
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    # Testaa, että lisäys lisää varaston saldoa oikein
    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    # Testaa, että lisäys pienentää varaston vapaata tilaa oikein.
    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    # Testaa, että ottaminen lisää tilaa varastossa oikein.
    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #Testaa, että lisäys ei lisää saldoa yli varaston tilavuuden.
    def test_lisays_ei_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    #Testaa, että ottaminen ei ota enempää kuin mitä varastossa on.
    def test_ottaminen_ei_ota_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Testaa, että negatiivisen määrän lisäys ei muuta saldoa.
    def test_lisays_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Testaa, että negatiivisen määrän ottaminen ei muuta saldoa.
    def test_ottaminen_negatiivinen_maara(self):
        saatu_maara = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu_maara, 0)

    #Testaa, että lisäys ei ylitä varaston tilavuutta.
    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    #Testaa, että ottaminen ei ylitä varaston saldoa.
    def test_ottaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Testaa, että negatiivinen tilavuus asetetaan nollaksi konstruktorissa
    def test_konstruktori_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    #Testaa, että negatiivinen alku saldo asetetaan nollaksi konstruktorissa.
    def test_konstruktori_negatiivinen_alku_saldo(self):
        varasto = Varasto(10, -10)
        self.assertAlmostEqual(varasto.saldo, 0)

    #Testaa, että alku saldo ei ylitä varaston tilavuutta konstruktorissa
    def test_konstruktori_alku_saldo_yli_tilavuuden(self):
        varasto = Varasto(10, 20)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_str_metodi(self):
        self.assertEqual(str(self.varasto), "saldo = 0.0, vielä tilaa 10.0")
