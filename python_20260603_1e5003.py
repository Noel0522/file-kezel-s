#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programozási nyelvek fájl átalakító
Feladat: Csak a nyelv neve és az évszám maradjon a fájlban
"""

def atalakit(forras_fajlnev='programozasi_nyelvek.txt', cel_fajlnev='nyelvek_evszamok.txt'):
    """
    Átalakítja a forrásfájlt úgy, hogy csak a nyelv és az évszám marad.
    
    Paraméterek:
    forras_fajlnev: str - a beolvasandó fájl neve
    cel_fajlnev: str - a létrehozandó fájl neve
    """
    try:
        # Fájlok megnyitása - olvasás és írás módban
        with open(forras_fajlnev, 'r', encoding='utf-8') as forrasfajl, \
             open(cel_fajlnev, 'w', encoding='utf-8') as celfajl:
            
            sorok_szama = 0
            feldolgozott_sorok = 0
            
            print(f"Feldolgozás: {forras_fajlnev} -> {cel_fajlnev}")
            
            # Sorról sorra olvassuk a forrásfájlt
            for sor in forrasfajl:
                sorok_szama += 1
                sor = sor.strip()
                
                # Üres sorok kihagyása
                if not sor:
                    continue
                
                # Kísérlet a sor felbontására különböző elválasztókkal
                talalat = False
                for elvalaszto in [' - ', ': ', ', ', '; ', ' ', '\t']:
                    if elvalaszto in sor:
                        reszek = sor.split(elvalaszto)
                        if len(reszek) >= 2:
                            nyelv = reszek[0].strip()
                            evszam = reszek[1].strip()
                            
                            # Evszám ellenőrzése (csak számokat és mínusz jelet tartalmazhat)
                            if evszam.replace('-', '').replace('/', '').isdigit():
                                # Csak az évszám első 4 karaktere (ha hosszabb)
                                if len(evszam) > 4 and evszam[:4].isdigit():
                                    evszam = evszam[:4]
                                
                                celfajl.write(f"{nyelv} - {evszam}\n")
                                feldolgozott_sorok += 1
                                talalat = True
                                break
                
                # Ha nem sikerült felbontani, mentsük el az eredeti sort (opcionális)
                if not talalat:
                    # Kommenteld ki a következő sort, ha nem akarod az ismeretlen formátumú sorokat
                    # celfajl.write(f"{sor} (ismeretlen formátum)\n")
                    print(f"Figyelmeztetés: Ismeretlen formátum a {sorok_szama}. sorban: {sor}")
                    feldolgozott_sorok += 1
            
            # Eredmény kiírása
            print(f"\nKész! Összesen {sorok_szama} sor volt a forrásfájlban.")
            print(f"{feldolgozott_sorok} sor került a '{cel_fajlnev}' fájlba.")
            
    except FileNotFoundError:
        print(f"\nHiba: A '{forras_fajlnev}' fájl nem található!")
        print("Kérlek, töltsd le először a forrásfájlt a feladat oldaláról.")
        print("Tipp: A 'Forrásfájl' gombra jobb klikk -> 'Link mentése másként...'")
    except PermissionError:
        print(f"\nHiba: Nincs jogosultság a '{forras_fajlnev}' fájl olvasásához vagy a '{cel_fajlnev}' létrehozásához!")
    except Exception as e:
        print(f"\nVáratlan hiba történt: {e}")


def main():
    """Fő függvény - felhasználói interakciók kezelése"""
    print("=" * 50)
    print("PROGRAMOZÁSI NYELVEK FÁJL ÁTALAKÍTÓ")
    print("=" * 50)
    print("\nEz a program beolvas egy fájlt programozási nyelvekről,")
    print("és átalakítja úgy, hogy csak a nyelv neve és az évszám marad benne.\n")
    
    # Fájlnevek bekérése a felhasználótól
    forras = input("Add meg a forrásfájl nevét [programozasi_nyelvek.txt]: ").strip()
    if not forras:
        forras = 'programozasi_nyelvek.txt'
    
    cel = input("Add meg a célfájl nevét [nyelvek_evszamok.txt]: ").strip()
    if not cel:
        cel = 'nyelvek_evszamok.txt'
    
    print()  # Üres sor a jobb olvashatóságért
    
    # Átalakítás végrehajtása
    atalakit(forras, cel)
    
    print("\nNyomj Enter-t a kilépéshez...")
    input()


# Program indítása
if __name__ == "__main__":
    main()