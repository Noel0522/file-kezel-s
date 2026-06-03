#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FÁJLBEO LVASÁS FELADATOK MEGOLDÁSA
Feladat: Programozási nyelvek és vers beolvasása, feldolgozása
"""

import string

def first_task(forras_fajlnev='programozasi_nyelvek.txt'):
    """
    1. feladat: Programozási nyelvek beolvasása
    a) list of dictionaries (szótárak listája)
    b) 2D list (kétdimenziós lista)
    """
    print("=" * 60)
    print("1. FELADAT: Programozási nyelvek beolvasása")
    print("=" * 60)
    
    try:
        with open(forras_fajlnev, 'r', encoding='utf-8') as fajl:
            # Adatok tárolása
            szotarak_listaja = []  # a) szótárak listája
            ketdimenzios_lista = []  # b) kétdimenziós lista
            
            for sor in fajl:
                sor = sor.strip()
                if not sor:  # üres sorok kihagyása
                    continue
                
                # Különböző elválasztók kezelése
                for elvalaszto in [' - ', ': ', ', ', '; ', '\t']:
                    if elvalaszto in sor:
                        reszek = sor.split(elvalaszto)
                        if len(reszek) >= 2:
                            nyelv = reszek[0].strip()
                            evszam_str = reszek[1].strip()
                            
                            # Csak az évszám szám részének kinyerése (pl. "1991." -> "1991")
                            evszam = ''
                            for karakter in evszam_str:
                                if karakter.isdigit() or (karakter == '-' and not evszam):
                                    evszam += karakter
                                else:
                                    break
                            
                            # Évszám konvertálása int típusúvá
                            try:
                                evszam_int = int(evszam)
                            except ValueError:
                                evszam_int = 0  # hibás évszám esetén 0
                            
                            # a) Szótár hozzáadása a listához
                            szotarak_listaja.append({
                                'nyelv': nyelv,
                                'evszam': evszam_int
                            })
                            
                            # b) Kétdimenziós listához hozzáadás
                            ketdimenzios_lista.append([nyelv, evszam_int])
                            
                            break
            
            # Eredmények kiírása
            print(f"\na) Szótárak listája ({len(szotarak_listaja)} elem):")
            for item in szotarak_listaja[:5]:  # csak első 5 elem
                print(f"   {item}")
            if len(szotarak_listaja) > 5:
                print(f"   ... és további {len(szotarak_listaja) - 5} elem")
            
            print(f"\nb) Kétdimenziós lista ({len(ketdimenzios_lista)} elem):")
            for item in ketdimenzios_lista[:5]:
                print(f"   {item}")
            if len(ketdimenzios_lista) > 5:
                print(f"   ... és további {len(ketdimenzios_lista) - 5} elem")
            
            return szotarak_listaja, ketdimenzios_lista
    
    except FileNotFoundError:
        print(f"\nHiba: A '{forras_fajlnev}' fájl nem található!")
        print("Kérlek, töltsd le a forrásfájlt a feladat oldaláról.")
        return None, None
    except Exception as e:
        print(f"\nHiba történt: {e}")
        return None, None


def second_task(vers_fajlnev='parduc.txt'):
    """
    2. feladat: Vers elemzése a read() metódussal
    Kérdések:
    - hány betűt tartalmaz a vers
    - hány magánhangzót tartalmaz a vers
    - hány szó fordul elő a versben
    """
    print("\n" + "=" * 60)
    print("2. FELADAT: Rilke: A párduc - vers elemzése")
    print("=" * 60)
    
    # Magánhangzók halmaza (magyar és angol)
    maganhangzok = set('aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ')
    
    try:
        with open(vers_fajlnev, 'r', encoding='utf-8') as fajl:
            # A teljes fájl tartalmának beolvasása read() metódussal
            teljes_tartalom = fajl.read()
            
            # 1. Hány betűt tartalmaz a vers?
            betuk_szama = sum(1 for karakter in teljes_tartalom if karakter.isalpha())
            
            # 2. Hány magánhangzót tartalmaz a vers?
            maganhangzok_szama = sum(1 for karakter in teljes_tartalom if karakter in maganhangzok)
            
            # 3. Hány szó fordul elő a versben?
            # Szavakra bontás: whitespace-ek és írásjelek mentén
            szavak = []
            aktualis_szo = ''
            for karakter in teljes_tartalom:
                if karakter.isalpha() or karakter == '-':  # betűk és kötőjelek a szó részei
                    aktualis_szo += karakter
                elif karakter.isdigit():
                    aktualis_szo += karakter  # számok is lehetnek a szóban
                else:
                    if aktualis_szo:  # ha van aktuális szó, mentsük el
                        szavak.append(aktualis_szo.lower())  # kisbetűsítve tároljuk
                        aktualis_szo = ''
            # Utolsó szó hozzáadása
            if aktualis_szo:
                szavak.append(aktualis_szo.lower())
            
            szavak_szama = len(szavak)
            
            # Eredmények kiírása
            print(f"\nA vers elemzésének eredményei:")
            print(f"  - Betűk száma: {betuk_szama}")
            print(f"  - Magánhangzók száma: {maganhangzok_szama}")
            print(f"  - Szavak száma: {szavak_szama}")
            
            # Extra információk (csak érdekességképp)
            print(f"\nExtra információk:")
            print(f"  - Karakterek száma (szóközökkel): {len(teljes_tartalom)}")
            print(f"  - Karakterek száma (szóközök nélkül): {len(teljes_tartalom.replace(' ', '').replace('\n', ''))}")
            print(f"  - Sortörések száma: {teljes_tartalom.count(chr(10))}")
            
            # Az első néhány szó megjelenítése
            print(f"\nAz első 10 szó a versből:")
            print(f"  {' '.join(szavak[:10])}...")
            
            return {
                'betuk': betuk_szama,
                'maganhangzok': maganhangzok_szama,
                'szavak': szavak_szama,
                'teljes_szoveg': teljes_tartalom
            }
    
    except FileNotFoundError:
        print(f"\nHiba: A '{vers_fajlnev}' fájl nem található!")
        print("Kérlek, töltsd le a vers fájlt a feladat oldaláról.")
        return None
    except Exception as e:
        print(f"\nHiba történt: {e}")
        return None


def main():
    """Fő függvény - felhasználói interakciók kezelése"""
    print("\n" + "=" * 60)
    print("FÁJLBEOLVASÁSI FELADATOK MEGOLDÁSA")
    print("=" * 60)
    
    # 1. feladat futtatása
    print("\nA feladat megoldásához szükség van a 'programozasi_nyelvek.txt' fájlra.")
    print("Ha még nincs meg, töltsd le a feladat oldaláról.\n")
    
    valasz = input("Szeretnéd futtatni az 1. feladatot? (i/n): ").strip().lower()
    if valasz in ['i', 'igen', 'y', 'yes']:
        fajlnev = input("Add meg a forrásfájl nevét [programozasi_nyelvek.txt]: ").strip()
        if not fajlnev:
            fajlnev = 'programozasi_nyelvek.txt'
        first_task(fajlnev)
    else:
        print("1. feladat kihagyva.")
    
    # 2. feladat futtatása
    print("\n" + "-" * 60)
    print("A 2. feladathoz szükség van a verset tartalmazó fájlra (pl. 'parduc.txt').")
    
    valasz2 = input("\nSzeretnéd futtatni a 2. feladatot? (i/n): ").strip().lower()
    if valasz2 in ['i', 'igen', 'y', 'yes']:
        vers_fajl = input("Add meg a vers fájl nevét [parduc.txt]: ").strip()
        if not vers_fajl:
            vers_fajl = 'parduc.txt'
        second_task(vers_fajl)
    else:
        print("2. feladat kihagyva.")
    
    print("\n" + "=" * 60)
    print("Program vége!")
    input("\nNyomj Enter-t a kilépéshez...")


# Program indítása
if __name__ == "__main__":
    main()