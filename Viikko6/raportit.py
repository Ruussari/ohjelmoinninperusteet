# Copyright (c) 2025 Sari Ruuskanen
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date, timedelta

def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi

    Parametrit:
     tietue: Sisältää 7 kenttää, joista ensimmäinen date -> loput int

    Palautus:
     Listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",",".")),
        float(tietue[2].replace(",",".")),
        float(tietue[3].replace(",",".")),
    ]


def lue_data(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä.

    Kutsuu funktiota muunna_tiedot (lst):
     funktio palauttaa listan -> Tietotyypit muutettu

    Parametrit:
     tiedoston_nimi (str): ottaa vastaan tiedoston, jossa kentät jaettu merkillä ;

    Palautus:
     tietokanta (lst): palauttaa tietokannan, jossa tietotyypit on muutettu
    """
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Otetaan kenttien esittelytiedot pois
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta

def raportti_tiedostoon(raportti: str):
    """
    Kirjoittaa annetun sisällön tiedostoon

    Parametrit:
    raportti (str): raporttiteksti
    """
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)

def raportti_aikavali(alkupaiva: str, loppupaiva: str, tietokanta: list) -> str:
    """
    Luo raportin aikaväliltä.
    Parametrit: 
    alkupaiva (str): aikavälin aloituspäivä
    loppupaiva (str): aikavälin lopetuspäivä
    tietokanta (list): sisältää kaikki tietueet
    Palautus:
    raportti (list): palauttaa luodun raportin
    """
    alku = datetime.strptime(alkupaiva, "%d.%m.%Y").date()
    loppu = datetime.strptime(loppupaiva, "%d.%m.%Y").date()

    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        if alku <= tietue[0].date() <= loppu:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1
    raportti = "******************************************\n"
    raportti += f"Alku- ja loppupäivä: {alkupaiva}-{loppupaiva}\n"
    raportti +="- Kokonaiskulutus: " + f"{kulutus:.2f}".replace(".", ",") + " kWh\n"
    raportti +="- Kokonaistuotanto: " + f"{tuotanto:.2f}".replace(".", ",") + " kWh\n"
    raportti +="- Aikavälin keskilämpötila: " + f"{lampotila/tietue_lkm:.2f}".replace(".", ",") + " °C\n"
    raportti += "******************************************"
    return raportti

def raportti_kuukausi(kuukausi: str, tietokanta: list) -> str:
    """
    Luo raportin kuukaudelle

    Parametrit: 
    kuukausi (str): pyydetty kuukausi
    tietokanta (list): sisältää kaikki tietueet
    
    Palautus:
    raportti (list): palauttaa luodun raportin
    """
    kuukaudet = [
        "Tammikuu", 
        "Helmikuu", 
        "Maaliskuu", 
        "Huhtikuu", 
        "Toukokuu", 
        "Kesäkuu", 
        "Heinäkuu", 
        "Elokuu", 
        "Syyskuu", 
        "Lokakuu", 
        "Marraskuu", 
        "Joulukuu"
    ]
    kk = int(kuukausi)
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        if tietue[0].date().month == kk:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1
    raportti = "******************************************\n"
    raportti += f"Raportti kuukaudelta: {kuukaudet[kk-1]}\n"
    raportti +="- Kokonaiskulutus: " + f"{kulutus:.2f}".replace(".", ",") + " kWh\n"
    raportti +="- Kokonaistuotanto: " + f"{tuotanto:.2f}".replace(".", ",") + " kWh\n"
    raportti +="- Aikavälin keskilämpötila: " + f"{lampotila/tietue_lkm:.2f}".replace(".", ",") + " °C\n"
    raportti += "******************************************"
    return raportti

def raportti_vuosi(tietokanta: list) -> str:
    """
    Luo raportin koko vuodelle

    Parametrit: 
    tietokanta (list): sisältää kaikki tietueet
    
    Palautus:
    raportti (list): palauttaa luodun raportin
    """
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        kulutus += tietue[1]
        tuotanto += tietue[2]
        lampotila += tietue[3]
        tietue_lkm += 1

    raportti = "******************************************\n"
    raportti += f"Raportti vuodelta 2025\n"
    raportti +="- Kokonaiskulutus: " + f"{kulutus:.2f}".replace(".", ",") + " kWh\n"
    raportti +="- Kokonaistuotanto: " + f"{tuotanto:.2f}".replace(".", ",") + " kWh\n"
    raportti +="- Vuoden keskilämpötila: " + f"{lampotila/tietue_lkm:.2f}".replace(".", ",") + " °C\n"
    raportti += "******************************************"
    return raportti

def main():
    """
    Ohjelman pääfunktio: Kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    kulutusTuotanto2025 = lue_data("2025.csv")

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")

        try:
            ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        except ValueError:
            print("Virhe: syötä numero väliltä 1–4.\n")
            continue

        if ensimmainen_valinta == 1:
            try:
                alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
                loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            except ValueError:
                print("Virhe: päivämäärän tulee olla muodossa pv.kk.vvvv.\n")
                continue

            print("Raportti aikaväliltä tulostuu.")
            raportti = raportti_aikavali(alkupaiva, loppupaiva, kulutusTuotanto2025)
            print(raportti)

        elif ensimmainen_valinta == 2:
            try:
                kuukausi = int(input("Anna kuukauden numero (1-12): "))
                if not 1 <= kuukausi <= 12:
                    raise ValueError
            except ValueError:
                print("Virhe: kuukauden tulee olla numero väliltä 1–12.\n")
                continue

            raportti = raportti_kuukausi(kuukausi, kulutusTuotanto2025)
            print(raportti)

        elif ensimmainen_valinta == 3:
            raportti = raportti_vuosi(kulutusTuotanto2025)
            print(raportti)

        elif ensimmainen_valinta == 4:
            print("Lopetetaan ohjelma.")
            break

        else:
            print("Virheellinen valinta.\n")
            continue

        # Toinen valikko
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")

        try:
            toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        except ValueError:
            print("Virhe: syötä numero väliltä 1–3.\n")
            continue

        if toinen_valinta == 1:
            print("Raportti kirjoitetaan tiedostoon.")
            raportti_tiedostoon(raportti)

        elif toinen_valinta == 2:
            continue

        elif toinen_valinta == 3:
            print("Lopetetaan ohjelma.")
            break

        else:
            print("Virheellinen valinta.\n")
            continue

if __name__ == "__main__":
    main()
