# Copyright (c) 2025 Sari Ruuskanen
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.

from datetime import datetime, date

def muunna_tiedot(kulutusTuotanto: list) -> list:
    """Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi"""
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(int(kulutusTuotanto[1]))
    muutettu_tietorivi.append(int(kulutusTuotanto[2]))
    muutettu_tietorivi.append(int(kulutusTuotanto[3]))
    muutettu_tietorivi.append(int(kulutusTuotanto[4]))
    muutettu_tietorivi.append(int(kulutusTuotanto[5]))
    muutettu_tietorivi.append(int(kulutusTuotanto[6]))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> list:
    """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä."""
    kulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f) # Otetaan sarakkaiden esittelytieto pois
        for kulutusTuotantoTieto in f:
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet))

    return kulutusTuotantoTiedot

def paivantiedot(paiva: str, lukemat: list) -> int:
    pv = int(paiva.split('.')[0])
    kk = int(paiva.split('.')[1])
    vuosi = int(paiva.split('.')[2])
    lasketutTiedot = []
    kulutus1vaihe = 0
    kulutus2vaihe = 0
    kulutus3vaihe = 0
    tuotanto1vaihe = 0
    tuotanto2vaihe = 0
    tuotanto3vaihe = 0
    for lukema in lukemat:
        if lukema[0].date() == date(vuosi, kk, pv):
            kulutus1vaihe += lukema[1]
            kulutus2vaihe += lukema[2]
            kulutus3vaihe += lukema[3]
            tuotanto1vaihe += lukema[4]
            tuotanto2vaihe += lukema[5]
            tuotanto3vaihe += lukema[6]
    
    lasketutTiedot.append(kulutus1vaihe/1000)
    lasketutTiedot.append(kulutus2vaihe/1000)
    lasketutTiedot.append(kulutus3vaihe/1000)
    lasketutTiedot.append(tuotanto1vaihe/1000)
    lasketutTiedot.append(tuotanto2vaihe/1000)
    lasketutTiedot.append(tuotanto3vaihe/1000)
    return lasketutTiedot


def main():
    """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
    lukemat = lue_data("viikko42.csv")
    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä         Pvm         Kulutus [kWh]                 Tuotanto [kWh]")
    print("             (pv.kk.vvvv)   v1          v2      v3      v1     v2     v3")
    print("---------------------------------------------------------------------------")
    maanantainlukemat = paivantiedot("13.10.2025", lukemat)
    print(f"Maanantai     13.10.2025   ", f"{maanantainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[5]:.2f}".replace('.', ','))
    tiistainlukemat = paivantiedot("14.10.2025", lukemat)
    print(f"Tiistai       14.10.2025   ", f"{tiistainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{tiistainlukemat[5]:.2f}".replace('.', ','))
    keskiviikonlukemat = paivantiedot("15.10.2025", lukemat)
    print(f"Keskiviikko   15.10.2025   ", f"{keskiviikonlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikonlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikonlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikonlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikonlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{keskiviikonlukemat[5]:.2f}".replace('.', ','))
    torstainlukemat = paivantiedot("16.10.2025", lukemat)
    print(f"Torstai       16.10.2025   ", f"{torstainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{torstainlukemat[5]:.2f}".replace('.', ','))
    perjantainlukemat = paivantiedot("17.10.2025", lukemat)
    print(f"Perjantai     17.10.2025   ", f"{perjantainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{perjantainlukemat[5]:.2f}".replace('.', ','))
    lauantainlukemat = paivantiedot("18.10.2025", lukemat)
    print(f"Lauantai      18.10.2025   ", f"{lauantainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{lauantainlukemat[5]:.2f}".replace('.', ','))
    sunnuntainlukemat = paivantiedot("19.10.2025", lukemat)
    print(f"Sunnuntai     19.10.2025   ", f"{sunnuntainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{sunnuntainlukemat[5]:.2f}".replace('.', ','))
    


if __name__ == "__main__":
    main()