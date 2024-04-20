from varasto import Varasto
#muokattiin index siten että jokainen tulostus omassa funktiossa

def tulosta_varastot(mehu, olut):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")

def tulosta_olut_getterit(olut):
    print("Olut getterit:")
    print(f"saldo = {olut.saldo}")
    print(f"tilavuus = {olut.tilavuus}")
    print(f"paljonko_mahtuu = {olut.paljonko_mahtuu()}")

def tulosta_mehu_setterit(mehu):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu}")
    print("Otetaan 3.14")
    mehu.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu}")

def tulosta_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50)")
    huono = Varasto(100.0, -50)
    print(huono)

def tulosta_oluttoimenpiteet(olut, mehu):
    print(f"Olutvarasto: {olut}")
    print("olutta.lisaa_varastoon(1000.0)")
    olut.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olut}")

    print(f"Mehuvarasto: {mehu}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehu.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehu}")

def tulosta_mehutoimenpiteet(mehu):
    print(f"Mehuvarasto: {mehu}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehu.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehu}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20)

    tulosta_varastot(mehua, olutta)
    tulosta_olut_getterit(olutta)
    tulosta_mehu_setterit(mehua)
    tulosta_virhetilanteet()
    tulosta_oluttoimenpiteet(olutta, mehua)
    tulosta_mehutoimenpiteet(mehua)

if __name__ == "__main__":
    main()
