# Copyright (c) 2025 Sari Ruuskanen
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date


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
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
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


def paivantiedot(paiva: date, tietokanta: list) -> list:
    """
    Laskee kulutus- ja tuotantotiedot vaiheittain ja palauttaa listan
    Laskettavat tiedot muutetaan Wh -> kWh

    Parametrit:
     paiva (date): Raportoitava päivä
     tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät

    Palautus:
     Listan, jossa tulostettavat merkkijonot
    """
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for tietue in tietokanta:
        if tietue[0].date() == paiva:
            kulutus[0] += tietue[1] / 1000
            kulutus[1] += tietue[2] / 1000
            kulutus[2] += tietue[3] / 1000
            tuotanto[0] += tietue[4] / 1000
            tuotanto[1] += tietue[5] / 1000
            tuotanto[2] += tietue[6] / 1000

    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    ]



def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
    """
    kulutusTuotantoViikko41 = lue_data("viikko41.csv")
    kulutusTuotantoViikko42 = lue_data("viikko42.csv")
    kulutusTuotantoViikko43 = lue_data("viikko43.csv")
    #viikko 41
    viikko41 = "\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko41 += "Päivä\t\t\t\tPvm\t\t Kulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko41 += "\t\t\t\t(pv.kk.vvvv) v1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko41 += "---------------------------------------------------------------------------\n"
    viikko41 += "maanantai\t" + "\t" + "\t".join(paivantiedot(date(2025, 10, 6), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "tiistai\t\t\t" + "\t".join(paivantiedot(date(2025, 10, 7), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "keskiviikko\t\t" + "\t".join(paivantiedot(date(2025, 10, 8), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "torstai\t\t\t" + "\t".join(paivantiedot(date(2025, 10, 9), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "perjantai\t\t" + "\t".join(paivantiedot(date(2025, 10, 10), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "lauantai\t\t" + "\t".join(paivantiedot(date(2025, 10, 11), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "sunnuntai\t\t" + "\t".join(paivantiedot(date(2025, 10, 12), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "---------------------------------------------------------------------------\n"
    #viikko 42
    viikko42 = "\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko42 += "Päivä\t\t\t\tPvm\t\t Kulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko42 += "\t\t\t\t(pv.kk.vvvv) v1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko42 += "---------------------------------------------------------------------------\n"
    viikko42 += "maanantai\t" + "\t" + "\t".join(paivantiedot(date(2025, 10, 13), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "tiistai\t\t\t" + "\t".join(paivantiedot(date(2025, 10, 14), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "keskiviikko\t\t" + "\t".join(paivantiedot(date(2025, 10, 15), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "torstai\t\t\t" + "\t".join(paivantiedot(date(2025, 10, 16), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "perjantai\t\t" + "\t".join(paivantiedot(date(2025, 10, 17), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "lauantai\t\t" + "\t".join(paivantiedot(date(2025, 10, 18), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "sunnuntai\t\t" + "\t".join(paivantiedot(date(2025, 10, 19), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "---------------------------------------------------------------------------\n"
    #viikko 43
    viikko43 = "\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko43 += "Päivä\t\t\t\tPvm\t\t Kulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko43 += "\t\t\t\t(pv.kk.vvvv) v1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko43 += "---------------------------------------------------------------------------\n"
    viikko43 += "maanantai\t" + "\t" + "\t".join(paivantiedot(date(2025, 10, 20), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "tiistai\t\t\t" + "\t".join(paivantiedot(date(2025, 10, 21), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "keskiviikko\t\t" + "\t".join(paivantiedot(date(2025, 10, 22), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "torstai\t\t\t" + "\t".join(paivantiedot(date(2025, 10, 23), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "perjantai\t\t" + "\t".join(paivantiedot(date(2025, 10, 24), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "lauantai\t\t" + "\t".join(paivantiedot(date(2025, 10, 25), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "sunnuntai\t\t" + "\t".join(paivantiedot(date(2025, 10, 26), kulutusTuotantoViikko43)) + "\n"
    #kirjoitetaan jotain tiedostoon
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)
        
if __name__ == "__main__":
    main()