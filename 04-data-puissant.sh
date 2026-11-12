#!/bin/bash
# 04 DATA - Puissant : je refuse le prix incomplet, je protege la verite
CSV=~/07-metier-digital/projets/prix-locaux/prix-locaux.csv
echo "=== 04 DATA - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Structure ---"
head -1 "$CSV"
echo "--- 2. Je verifie chaque prix, ligne par ligne ---"
python3 << 'PY'
import csv, pathlib
csv_path = pathlib.Path("/root/07-metier-digital/projets/prix-locaux/prix-locaux.csv")
rows = list(csv.DictReader(open(csv_path)))
print(f"Prix reels : {len(rows)}")
if not rows:
    print("OK : 0 prix, 0 erreur. Base propre, j'attends le reel.")
else:
    erreurs = 0
    for i, r in enumerate(rows, start=2):
        manquants = [k for k in ["date","produit","categorie","region","ville","lieu","prix_ar","source","vu_par"] if not (r.get(k) or "").strip()]
        if manquants:
            print(f"Ligne {i} REFUSEE - manque : {', '.join(manquants)}")
            erreurs += 1
        try:
            p = float(r.get("prix_ar") or 0)
            if p <= 0:
                print(f"Ligne {i} REFUSEE - prix <= 0")
                erreurs += 1
        except:
            print(f"Ligne {i} REFUSEE - prix pas un nombre")
            erreurs += 1
    if erreurs == 0:
        print(f"OK : {len(rows)} prix, tous complets, tous valides. Qualite 100/100.")
    else:
        print(f"ALERTE : {erreurs} ligne(s) a corriger, je ne les laisse pas passer.")
PY
echo "--- 3. Regions couvertes (reel) ---"
tail -n +2 "$CSV" | cut -d, -f4 | sort -u | grep -v "^$" | wc -l
echo "--- 4. Produits distincts (reel) ---"
tail -n +2 "$CSV" | cut -d, -f2 | sort -u | grep -v "^$" | wc -l
echo "=== FIN 04 - Qualite 100/100 ou je bloque ==="
